# benvalla.github.io — missing CSS / JS / assets fix

Your live HTML references **`css/styles.css`**, **`js/main.js`**, and files under **`assets/`**, but those paths were not present in the repository, so browsers returned **404** for the stylesheet (unstyled pages) and scripts.

This folder contains everything to add.

## Copy into your site repo

1. Clone **`https://github.com/benvalla/benvalla.github.io`** (or open it locally).
2. Merge these folders into the **repository root** (next to `index.html`):
   - `css/` → `css/`
   - `js/` → `js/`
   - `assets/illustrations/` → `assets/illustrations/` (creates `assets` if needed)

3. **Logo & CV paths** expected by your HTML:
   - `assets/logos/jll.png`, `tetris.png`, `accenture.png`, `bouygues.png`
   - `assets/Benoit-Valla-CV.pdf`

   From the repo root in **PowerShell**, run:

   ```powershell
   .\scripts\sync-assets-from-root.ps1
   ```

   (If you copied this fix into the repo, the script is at `scripts/sync-assets-from-root.ps1`.)

   The script copies the logo/CV files that already exist at the **root** of the repo (e.g. `JLL_logo.svg.png`) into `assets/` with the names your HTML uses.

4. Commit and push:

   ```bash
   git add css js assets scripts
   git status
   git commit -m "Add site CSS, JS, illustrations, and synced asset paths"
   git push
   ```

5. After GitHub Pages rebuilds (~1–2 minutes), hard-refresh the site (**Ctrl+F5**).

## What was added

| Path | Role |
|------|------|
| `css/styles.css` | Layout, typography, hero, timeline, skills tags, contact form, responsive nav |
| `js/main.js` | Mobile menu toggle; FormSubmit `_next` default for thank-you page |
| `assets/illustrations/*.svg` | Decorative illustrations referenced from HTML |
| `scripts/sync-assets-from-root.ps1` | Copies root logos/CV into `assets/` |

If any logo still 404s, check the filename at repo root and adjust the script or copy manually.
