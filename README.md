# Garrett Beck — Personal Portfolio

This repository is a static Jekyll site for `garrettbeck-sudo.github.io`. It is designed to publish directly through GitHub Pages from the `main` branch and the repository root (`/`).

## Update the site

- Edit `index.md`, `about.md`, `experience.md`, or `contact.md` to update page content.
- Shared page structure lives in `_layouts/default.html`.
- Shared navigation and footer live in `_includes/`.
- Visual styles live in `assets/css/style.css`.
- The theme toggle is the only JavaScript in the site and lives in `assets/js/theme.js`.
- Update `_config.yml` if the GitHub username, site description, or public contact details change.

Keep claims, dates, employers, numbers, and project details grounded in current source material. Do not add achievements or metrics that have not been supplied.

## Preview locally

Install Ruby and the Jekyll/Bundler tools for your system, then run:

```bash
gem install jekyll bundler
jekyll serve --livereload
```

Open `http://localhost:4000`. Since `baseurl` is intentionally empty for a GitHub user site, local page links use the same paths as production.

If Jekyll is not available, a static-only preview can be served with:

```bash
python3 -m http.server 5000
```

That fallback previews source files only and does not render Markdown or Liquid; use Jekyll for a complete preview.

## Publish with GitHub Pages

1. Push the repository to `garrettbeck-sudo/garrettbeck-sudo.github.io`.
2. In GitHub, open **Settings → Pages**.
3. Choose **Deploy from a branch**.
4. Select `main` and `/ (root)`, then save.
5. GitHub Pages will build the Jekyll site automatically at `https://garrettbeck-sudo.github.io`.

No manual build or deployment step is required.

## Check quality

With the site running, run Lighthouse in Chrome DevTools or with Lighthouse CLI:

```bash
npx lighthouse http://localhost:4000 --view
```

Check the mobile and desktop views. The target is 90 or higher in Performance, Accessibility, Best Practices, and SEO. Also confirm the pages render cleanly at 375px and 1280px widths.