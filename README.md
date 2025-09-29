# Loïc Miller - Academic CV

This repository hosts my academic CV website built with [Hugo](https://gohugo.io/) and the [theme-academic-cv](https://github.com/HugoBlox/theme-academic-cv) template.

The site is automatically deployed to GitHub Pages via GitHub Actions, and visitors are redirected to [https://loicmiller.com](https://loicmiller.com).



---
## 🚀 Local Development

1. **Clone the repository**

```bash
git clone https://github.com/loicmiller/loicmiller.git
cd loicmiller
```

2. **Install dependencies**

```bash
pnpm install
```

3. **Fix Hugo shortcodes (if missing)**

```bash
hugo mod clean
hugo mod get -u ./...
```

4. **Run the local server**

```bash
hugo server
```

Visit http://localhost:1313 to preview your site locally.



---
## 🛠 Modify Content

All content is in the content/ folder.

Configuration is in config.toml.

Theme settings are in the themes/theme-academic-cv folder.

Edit markdown files, add publications, projects, or update your CV, then rebuild the site locally to preview changes.



---
## 📦 Deployment

This site uses GitHub Actions for continuous deployment:

1. Push changes to the `main` branch.
2. GitHub Actions automatically builds the site using Hugo and deploys the static files from the `public/` folder to the `gh-pages` branch.
3. GitHub Pages automatically redirects visitors to https://loicmiller.com

The workflow file is located at .github/workflows/gh-pages.yml.


## ⚡ Notes

- Ensure your Hugo version matches the one specified in `.github/workflows/gh-pages.yml`.
- Do not push the `public/` folder manually; it is generated automatically during deployment.
- For more details on the theme and available shortcodes, see theme-academic-cv documentation