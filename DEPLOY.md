# Align this folder with `benvalla.github.io`

Remote: **https://github.com/benvalla/benvalla.github.io**

This folder is the full static site (`index.html`, `css/`, `js/`, `assets/`, etc.). The duplicate bundle `benoitvalla-github-pages-fix/` is listed in `.gitignore` and is **not** pushed.

## One-time setup (if `git init` is not done yet)

Open **PowerShell** or **Git Bash** in this directory:

```powershell
cd "c:\Users\benoit.valla\OneDrive - JLL\Home Drive Import\Perso\Career & co\benoitvalla.com"
```

## Connect to GitHub and push

### 1. Initialize and first commit (only if `.git` does not exist)

```powershell
git init
git branch -M main
git add -A
git status
git commit -m "Site: HTML, CSS, JS, assets, CNAME for GitHub Pages"
```

### 2. Add remote and merge remote history

```powershell
git remote add origin https://github.com/benvalla/benvalla.github.io.git
git fetch origin main
git merge origin/main --allow-unrelated-histories -m "Merge GitHub history with local site"
```

If Git reports **merge conflicts**, open the listed files, fix them (keep your local HTML/CSS/JS where unsure), then:

```powershell
git add -A
git commit -m "Resolve merge with origin/main"
```

**Alternative** if you intend to **replace** whatever is on GitHub with this folder exactly (overwrites remote `main`):

```powershell
git push -u origin main --force
```

Use `--force` only if you understand it rewrites `main` on GitHub.

### 3. Normal push (after merge succeeds)

```powershell
git push -u origin main
```

Sign in when prompted (browser or token). For **HTTPS** on Windows, use a [Personal Access Token](https://github.com/settings/tokens) as the password if asked.

### 4. Later updates

After editing files:

```powershell
git add -A
git status
git commit -m "Describe your change"
git push
```

## GitHub Pages

Repo: **Settings → Pages**: source **Deploy from branch** `main`, folder **`/` (root)**.

Custom domain: **`www.benoitvalla.com`** (matches root `CNAME`). Enable **Enforce HTTPS** after DNS is green.
