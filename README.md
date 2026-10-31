# Loïc Miller — academic website

Source of [loicmiller.com](https://loicmiller.com), built with [Hugo](https://gohugo.io/) and
[HugoBlox Kit](https://github.com/HugoBlox/kit) (academic CV template), deployed to GitHub Pages by GitHub Actions on
every push to `master`.

## Where things are

| What | File |
|---|---|
| Profile: bio, links, interests, education, experience, awards | `data/authors/admin.yaml` (`content/authors/admin/_index.md` holds the same profile in the older format) |
| Home page sections | `content/_index.md` |
| Papers | `content/publication/<slug>/` (`index.md`, `cite.bib`, PDF, `featured.jpg`) |
| Talks | `content/event/<slug>/` |
| Experience, Teaching | `content/experience.md`, `content/teaching/_index.md` |
| CV (« Download CV ») | `static/uploads/resume.pdf` |
| Site settings, menu | `config/_default/` |
| Hugo version | `hugoblox.yaml` (`build.hugo_version`), read by the workflow too |
| Deployment | `.github/workflows/hugo.yml` |

## Local preview and updates

Needs Node 22+ and pnpm. Hugo is downloaded by `scripts/toolchain.py`, at the version `hugoblox.yaml` names, so the
laptop builds exactly as GitHub does.

```bash
pnpm install
"$(python3 scripts/toolchain.py bin)" server          # preview on http://localhost:1313
python3 scripts/toolchain.py update                   # latest theme modules + Tailwind, newest Hugo that builds
```

`public/`, `resources/` and `node_modules/` are generated: never commit them. The search index (Pagefind) is built
after Hugo, by the workflow.
