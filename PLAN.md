# Garrett Beck Portfolio — Build Plan

## Site summary

Build a publish-ready personal portfolio for **Garrett Beck** as a GitHub Pages user site at:

`https://garrettbeck-sudo.github.io`

The repository root will contain the complete Jekyll site. There will be no nested app, backend, database, Node project, or separate preview application.

## Pages and content

- **Home** — concise introduction, leadership positioning, selected highlights, and calls to action for work history and contact.
- **About** — Garrett's professional summary, education, leadership values, and focus areas.
- **Work Experience** — chronological military and civilian experience from the supplied résumé, preserving supplied employers, dates, roles, responsibilities, and achievements without adding claims.
- **Contact** — public `mailto:garrett_beck@berkeley.edu` link, LinkedIn link, GitHub profile link, and a clear note that the email address is public.

Navigation and footer links will be shared through reusable Jekyll includes.

## Visual direction

- Light and dark themes with a user-controlled theme toggle and a system-preference default.
- Palette based on the supplied MIL MOVE preference: gold, black, white, and grey.
- Clean, modern typography with Poppins-like geometric character; use a privacy-friendly system fallback stack so the site remains self-contained and fast.
- Responsive single-column layout optimized for 375px phones through 1280px desktop widths.
- Accessible contrast, visible focus states, semantic landmarks, skip link, reduced-motion support, and keyboard-operable controls.

## Technical approach

- Markdown page content with YAML front matter.
- Reusable `_layouts/default.html`, `_includes/head.html`, `_includes/header.html`, `_includes/footer.html`, and `_includes/theme-toggle.html`.
- Root-level `_config.yml` with an empty `baseurl` and URL filters for GitHub Pages-safe links.
- Plain CSS in `assets/css/style.css`; minimal inline JavaScript only for theme preference and persistence.
- SEO metadata, Open Graph basics, `sitemap.xml`, `robots.txt`, and a simple SVG/favicon asset.
- README instructions for editing content, local Jekyll preview, GitHub Pages publishing from `main` and `/ (root)`, and Lighthouse checks.

## Content source and assumptions

- Professional content comes only from the résumé supplied in this conversation.
- The supplied résumé contains a Gmail address, but the explicit contact answer selected `garrett_beck@berkeley.edu`; the latter will be used for the public contact link.
- The LinkedIn URL will be linked as an external profile, not scraped or used as a source of personal claims.
- MIL MOVE is used as a visual reference only; no business claims will be added beyond the résumé.
- No headshot, logo, project case studies, or additional portfolio links were supplied. The design will use text and CSS only, with no invented project content.

## Approval gate

After approval, build the files directly in the repository root, then verify:

1. Jekyll configuration and Markdown pages are root-level and GitHub Pages-ready.
2. All navigation and external links work.
3. The site renders at 375px and 1280px widths.
4. The build completes without errors.
5. Lighthouse Performance, Accessibility, Best Practices, and SEO each target 90 or higher.