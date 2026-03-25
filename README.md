# benoitvalla.com

Static professional site for **Benoît Valla** — profile, experience, skills, and contact. Built for hosting on **GitHub Pages**.

**GitHub repository:** [benvalla/benvalla.github.io](https://github.com/benvalla/benvalla.github.io) · **`git push`** and merge steps: [DEPLOY.md](DEPLOY.md).

## Run locally

From this folder, serve over HTTP (so asset paths behave like production):

```bash
# Python 3
python -m http.server 8080
```

Then open `http://localhost:8080/`.

On Windows PowerShell you can also use:

```powershell
npx --yes serve .
```

## GitHub Pages

1. Push this repository to GitHub.
2. In the repo **Settings → Pages**, set **Source** to deploy from the branch that contains these files (often `main`), folder **`/` (root)**.
3. After the first deploy, open the contact form once: **FormSubmit** sends a one-time activation email to `benoitvalla90@gmail.com` — follow their link to enable submissions.
4. The thank-you redirect uses JavaScript to build an absolute URL to `thank-you.html`, which works for both `username.github.io` and `username.github.io/repository-name` layouts.

If you use a **custom domain**, no change is required for the redirect as long as the site is served from the same origin.

## Project layout

| Path | Purpose |
|------|---------|
| `index.html` | Home / hero |
| `experience.html` | Employment timeline |
| `skills.html` | Skills, languages, certifications |
| `about.html` | Profile and education |
| `contact.html` | Form (FormSubmit → Gmail) |
| `thank-you.html` | Post-submit landing |
| `credits.html` | Icon / illustration credits |
| `assets/logos/` | Employer & school logos (PNG, your files) |
| `assets/illustrations/` | Decorative SVGs |
| `css/styles.css` | Styles |
| `js/main.js` | Mobile nav, form redirect URL |
| `assets/Benoit-Valla-CV.pdf` | Downloadable CV (copy of your PDF) |
| `headshot_*.jpg` | Photos referenced by the pages |

## Updating content

- Edit the HTML pages to reflect CV changes.
- Replace `assets/Benoit-Valla-CV.pdf` when you update your CV (keep the same filename, or update every `href` that points to it).

## Privacy note

Phone number, postal address, and similar details from the CV are **not** shown on the site. The contact form delivers to the configured email via FormSubmit; the service URL appears in the form markup (required for that provider).
