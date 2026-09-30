# Change 1: Restore GitHub Pages publishing

## Goal

Make the public GitHub Pages site at `https://garrettbeck-sudo.github.io/` serve the current root-level Jekyll portfolio, including the redesigned profile layout and Garrett's portrait.

## Current findings

- The repository is `garrettbeck-sudo/garrettbeck-sudo.github.io`, and its `main` branch points to commit `7fcf547`.
- The latest GitHub Actions run for “pages build and deployment” completed successfully for that commit.
- The public site still serves the older homepage rather than the redesigned portfolio.
- The GitHub Pages REST endpoints checked during diagnosis returned `404`. This does not, by itself, establish which Pages source or setting is responsible.
- The local Jekyll build succeeds, and the redesigned pages work in the Replit preview.

## Scope and constraints

- Keep the website as a static Jekyll site rooted at the repository root.
- Preserve the existing GitHub Pages URL and current site content.
- Do not add a backend, database, JavaScript framework, or a second app.
- Do not change hosting providers or repository settings without confirming the intended Pages source.
- Do not put credentials or tokens in this file or in the repository.

## Plan

1. **Confirm the GitHub Pages source.** Check the repository's Pages settings and deployment details to determine whether it publishes `main` from the repository root or uses another source.
2. **Inspect the successful deployment.** Confirm that the Pages build for commit `7fcf547` generated the redesigned homepage and included `assets/images/garrett-beck.jpg`.
3. **Compare the build with the public site.** Determine whether the stale page comes from the selected source, a deployment artifact, a domain/CDN cache, or another Pages configuration issue.
4. **Apply the smallest targeted fix.** Change only the setting or Jekyll configuration identified in the previous steps. Keep the root-level Jekyll structure intact.
5. **Rebuild and publish.** Trigger a new Pages build from the intended source after the fix.
6. **Verify the public result.** Confirm the live homepage contains “Profile overview” and “Areas of focus,” loads the portrait, and no longer shows the old homepage heading. Check the About, Experience, and Contact pages as well.

## Acceptance criteria

- The public Pages URL serves the redesigned portfolio from the current `main` branch.
- The profile portrait and local CSS/JavaScript assets load successfully.
- The homepage and the About, Experience, and Contact routes return successful responses.
- The latest GitHub Pages deployment completes successfully.
- The change does not introduce a separate app or require a manual local build to publish.

## Open item

The exact Pages source and the reason the successful deployment is not reflected at the public URL still need to be confirmed before choosing a fix.