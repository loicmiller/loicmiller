#!/usr/bin/env python3
"""Hugo and HugoBlox Kit for this site: the pinned Hugo binary, and bringing both to their latest versions.

hugoblox.yaml (build.hugo_version) is the one place that names the Hugo version; the GitHub Actions workflow
reads it too, so the site builds the same on the laptop and on GitHub. Binaries live in ~/.local/bin/hugo-<v>
(official release archives, SHA-256 checked), never the snap's auto-updated `hugo`.

    python3 scripts/toolchain.py bin        # path to the pinned Hugo (downloaded if missing)
    python3 scripts/toolchain.py update     # latest theme modules + Tailwind, newest Hugo the site builds with

`update` tries the latest Hugo release first, then the version HugoBlox Kit recommends, then the current one,
and keeps the newest that builds the site; if none does, every file it touched is put back.
"""

import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
BIN_DIR = Path.home() / ".local" / "bin"
PIN = re.compile(r"""^(\s*hugo_version:\s*['"]?)([0-9.]+)(['"]?)""", re.M)
KIT_PIN = "https://raw.githubusercontent.com/HugoBlox/kit/main/templates/academic-cv/hugoblox.yaml"
RELEASES = "https://github.com/gohugoio/hugo/releases/download/v{v}/"
TOUCHED = ["go.mod", "go.sum", "package.json", "pnpm-lock.yaml", "hugoblox.yaml", "netlify.toml"]


def get(url: str, binary: bool = False):
    req = urllib.request.Request(url, headers={"User-Agent": "loicmiller-website-toolchain"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    return data if binary else data.decode()


def pinned() -> str:
    return PIN.search((SITE / "hugoblox.yaml").read_text()).group(2)


def hugo_bin(version: str) -> Path:
    """~/.local/bin/hugo-<version>, downloaded from the official release and checked against its checksums."""
    path = BIN_DIR / f"hugo-{version}"
    if path.exists():
        return path
    name = f"hugo_extended_{version}_linux-amd64.tar.gz"
    archive = get(RELEASES.format(v=version) + name, binary=True)
    sums = get(RELEASES.format(v=version) + f"hugo_{version}_checksums.txt")
    want = next(line.split()[0] for line in sums.splitlines() if line.endswith(name))
    if hashlib.sha256(archive).hexdigest() != want:
        sys.exit(f"checksum mismatch for {name}: not installed")
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        member = tar.getmember("hugo")
        BIN_DIR.mkdir(parents=True, exist_ok=True)
        path.write_bytes(tar.extractfile(member).read())
    path.chmod(0o755)
    print(f"installed {path}")
    return path


def builds(version: str) -> bool:
    with tempfile.TemporaryDirectory() as out:
        r = subprocess.run([str(hugo_bin(version)), "--gc", "--minify", "-d", out], cwd=SITE, capture_output=True, text=True)
    if r.returncode:
        err = next((line for line in (r.stdout + r.stderr).splitlines() if line.startswith("ERROR")), "build failed")
        print(f"  Hugo {version}: does not build — {err[:160]}")
    else:
        print(f"  Hugo {version}: builds")
    return r.returncode == 0


def set_pin(version: str) -> None:
    for name, rx in (("hugoblox.yaml", PIN), ("netlify.toml", re.compile(r'(HUGO_VERSION\s*=\s*")([0-9.]+)(")'))):
        p = SITE / name
        if p.exists():
            p.write_text(rx.sub(lambda m: m.group(1) + version + m.group(3), p.read_text(), count=1))


def key(v: str) -> tuple:
    return tuple(int(x) for x in v.split("."))


def update() -> int:
    before = {n: (SITE / n).read_text() for n in TOUCHED if (SITE / n).exists()}
    current = pinned()
    latest = json.loads(get("https://api.github.com/repos/gohugoio/hugo/releases/latest"))["tag_name"].lstrip("v")
    kit = PIN.search(get(KIT_PIN)).group(2)
    print(f"Hugo: pinned {current}, latest {latest}, recommended by HugoBlox Kit {kit}")
    print("Theme modules and Tailwind to their latest versions…")
    subprocess.run([str(hugo_bin(current)), "mod", "get", "-u"], cwd=SITE, check=True)
    subprocess.run(["pnpm", "update"], cwd=SITE, check=True)
    for v in sorted({latest, kit, current}, key=key, reverse=True):
        if builds(v):
            set_pin(v)
            break
    else:
        print("No Hugo version builds the site with the updated theme: everything is put back.")
        for n, text in before.items():
            (SITE / n).write_text(text)
        subprocess.run(["pnpm", "install"], cwd=SITE, check=False)
        return 1
    print(f"\nHugo {current} → {pinned()}")
    subprocess.run(["git", "--no-pager", "diff", "--stat", "--", *TOUCHED], cwd=SITE)
    print("Preview with `website`, then commit these files with your changes; GitHub builds with the same Hugo.")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "bin":
        print(hugo_bin(pinned()))
        return 0
    if cmd == "update":
        return update()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
