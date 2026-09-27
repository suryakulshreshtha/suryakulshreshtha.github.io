# Surya Kulshreshtha — terminal website

A personal site that looks like a terminal session. It types out a few commands, prints the profile, and ends with a passing `pytest` run.

Everything lives in **one file: `index.html`**. There is nothing to install and no build step. Edit the file, save, refresh.

---

## Putting the site online with GitHub Pages

You only need a web browser and a GitHub account. Everything below is done on github.com; no software to install.

**Before you start:** have `index.html` and `README.md` saved somewhere on your computer. The finished site will live at **https://suryakulshreshtha.github.io**.

### Step 1 — Create the repository

1. Sign in to github.com.
2. In the top-right corner of any page, click the **+** icon, then click **New repository**.
3. **Owner:** use the dropdown to pick your own account, `suryakulshreshtha`.
4. **Repository name:** type exactly:
   ```
   suryakulshreshtha.github.io
   ```
   The name must be your username followed by `.github.io`, all in lowercase. Any other name gives you a different web address (`suryakulshreshtha.github.io/<name>`) instead of the main one.
5. **Description:** optional, e.g. `Personal website`.
6. **Visibility:** choose **Public**. On a free GitHub account, Pages only works on public repositories. (Even on paid plans, the site itself is always public on the internet.)
7. Turn the **Add README** switch **On**. This creates the `main` branch straight away, which Step 3 needs.
8. Click **Create repository**.

### Step 2 — Upload the two files

1. You are now on the repository's main page. Click **Add file** (above the file list), then **Upload files**.
2. Drag `index.html` and `README.md` onto the page, or click **choose your files** and select them.
   - Your `README.md` replaces the empty one GitHub created in Step 1. That's expected.
   - `index.html` must sit at the top level of the repository, not inside a folder. GitHub Pages looks for a file called exactly `index.html` there as the site's home page.
3. Scroll down. In the commit message box, type something like `Add website`.
4. Leave **Commit directly to the main branch** selected and click **Commit changes**.

You should now see `index.html` and `README.md` listed on the repository page.

### Step 3 — Turn on GitHub Pages

1. On the repository page, click the **Settings** tab (the gear icon, in the row of tabs under the repository name). If you can't see it, click the **···** menu at the end of that row, then **Settings**.
2. In the left sidebar, under the **Code and automation** section, click **Pages**.
3. Under **Build and deployment**, find **Source** and choose **Deploy from a branch**.
4. Under **Branch**, open the first dropdown (it may say **None**) and pick **main**.
5. Open the folder dropdown next to it and pick **/ (root)**.
6. Click **Save**.

### Step 4 — Visit the site

1. Wait a few minutes. Publishing can take **up to 10 minutes**.
2. Go back to **Settings → Pages**. When it's ready, the top of that page shows your site's address with a **Visit site** button.
3. Click **Visit site**, or go straight to **https://suryakulshreshtha.github.io**.

Behind the scenes, GitHub publishes the site by running an automatic job. You can watch it under the repository's **Actions** tab: a yellow dot means it's still running, a green tick means it's live, a red cross means something failed (click it to see why).

### Step 5 (optional) — Skip GitHub's page builder

When publishing from a branch, GitHub runs every site through a tool called Jekyll by default. This site is plain HTML and doesn't need it. Skipping it makes publishing slightly faster and stops `README.md` from also being turned into a page on your site.

1. On the repository page, click **Add file → Create new file**.
2. Name the file exactly `.nojekyll` (starting with a dot, no extension). Leave the contents empty.
3. Click **Commit changes**, then **Commit changes** again in the pop-up.

### Updating the site later

**Quick edit in the browser:**
1. On the repository page, click `index.html`.
2. Click the **pencil icon** (Edit this file) at the top right of the file.
3. Make your change (see *Where to edit things* below).
4. Click **Commit changes**, add a short message, and click **Commit changes** again.

**Replace the whole file:** use **Add file → Upload files** again and upload the new `index.html`. It overwrites the old one.

Every change to the `main` branch republishes the site automatically; allow up to 10 minutes. If you still see the old version, do a hard refresh: **Ctrl+Shift+R** (Windows/Linux) or **Cmd+Shift+R** (Mac).

**Using git from a terminal instead?** Clone once, then edit, commit and push:

```bash
git clone https://github.com/suryakulshreshtha/suryakulshreshtha.github.io.git
cd suryakulshreshtha.github.io
# ...edit index.html...
git add .
git commit -m "Update site"
git push
```

### If the site doesn't appear

| What you see | What to check |
| --- | --- |
| A GitHub **404** page | The repository name is exactly `suryakulshreshtha.github.io`; `index.html` is at the top level (not in a folder) and spelled in lowercase; **Settings → Pages** shows branch `main` and folder `/ (root)`. |
| Nothing has changed after 10 minutes | Look at the **Actions** tab. If the latest run has a red cross, open it to read the error, then click **Re-run jobs**. |
| Still not publishing | The changes must be committed by an account with admin rights on the repository and a **verified email address**. Check your email is verified under your GitHub account's **Settings → Emails**. |
| Page loads but looks broken or blank | Open the browser console (**F12 → Console**) to find the line with the error. Usually a missing comma or quote from an edit. |
| Your README shows instead of the site | `index.html` is missing from the top level or has a different name, so GitHub fell back to the README. Re-upload it as `index.html`. |

---

## Previewing changes on your computer

Before uploading a change, double-click `index.html` on your computer to open it in a browser. After each edit, save and refresh.

If the page goes blank after an edit, a comma or quote is almost certainly out of place. Open the browser console (**F12 → Console**). The red error shows the line number to look at.

---

## Where to edit things

Line numbers drift as you edit, so each item below gives you a piece of text to **search for** (Ctrl+F / Cmd+F) instead.

### The prompt (`Callsign@Anti-Errorist`)

Search for: `var HOST`

```js
var HOST = 'Callsign@Anti-Errorist';
```

The part before `@` shows in the prompt colour and the `~` and `$` are added automatically.

### Browser tab title and search description

Search for: `<title>` and `name="description"`, near the top of the file.

### Tab icon (🧪)

Search for: `rel="icon"`. Swap the emoji inside `<text ...>🧪</text>` for any other single emoji.

### The commands that get typed, and what they print

Search for: `var steps`

```js
var steps = [
  { cmd: 'grep "root" /etc/group', out: '<span class="out c-name">surya kulshreshtha</span>' },
  { cmd: 'uname -a',               out: '<span class="out strong">sdet / test automation engineer — ...</span>' },
  { cmd: 'cd /home/surya/ && ls',  out: '<span class="out c-file strong">intro.txt</span>' },
  { cmd: 'cat intro.txt',          out: intro },
  { cmd: 'pytest tests/test_surya.py -q', out: ... }
];
```

- `cmd` is the text that gets typed after the prompt.
- `out` is what appears underneath. Change the words between `>` and `</span>`.
- To remove a command, delete its whole `{ ... },` line.
- To add one, copy an existing line and change the text.

The one-line bio is the `uname -a` output. The ending test result (`6 passed in 0.42s`) is the last entry.

### Everything printed by `cat intro.txt`

Search for: `var intro`. The sections below are all inside it, in the order they appear on the page.

#### Root variables and tech stack

These are the green `name = [...]` lines. Each line is one pair:

```js
['interests', list(['Test Automation', 'QA Architecture', 'CI/CD', 'Self-healing Tests'])],
```

- **Add a skill:** add `'NewThing'` inside the square brackets, separated by a comma.
- **Add a whole line:** copy a pair, paste it on a new line, change the name and the items. Every pair except the last needs a comma after `]`.
- **Single text value** (like `role` and `motto`) uses this form instead:
  ```js
  ['role', "'" + esc('SDET / Test Automation Engineer') + "'"],
  ```

#### Work experience

Search for: `section('WORK EXPERIENCE')`

Each job is one line:

```js
'<div class="row tagged"><span class="tag">[now]</span><span>' + link('https://www.protiviti.com', 'Protiviti') + '</span></div>' +
```

- Replace `[now]` / `[past]` with dates, e.g. `[2024–now]`. Tags longer than 6 characters need a wider column; see *Font, size and width* below.
- To add a job title before the company, change `</span><span>'` to `</span><span><b>SDET</b>, '` on that line.
- To add another job, copy a whole line (including the `+` at the end).

#### Projects

Search for: `var projects`

```js
var projects = [
  ['py', 'ForkablePlaywrightSelfHealer', 'Playwright tests that repair their own locators ...'],
  ...
];
```

Each project is `['language tag', 'ExactRepoName', 'short description']`. The repo name becomes the link, so it must match the GitHub repo name exactly. Order on the page is the order in this list.

#### Blog and contact links

Search for: `section('BLOG')` and `section('CONTACT')`

Each link looks like `link('https://address', 'label')`. Change the address, the label, or copy one to add another (keep the `' ] [ '` separators between them).

#### Adding a brand-new section

Inside `var intro`, add these two lines where you want the section to appear (note the commas):

```js
section('CERTIFICATIONS'),
'<div class="rows"><div class="row">ISTQB Foundation Level</div></div>',
```

---

## Look and feel

All styling is in the `<style>` block at the top of the file.

### Colours

The site follows the visitor's device setting: dark mode shows the original navy terminal, light mode shows a pale version.

| What | Variable |
| --- | --- |
| Background | `--bg` |
| Normal text | `--text` |
| `Callsign@Anti-Errorist` and `$` | `--host` |
| The `~` | `--path` |
| Your name (orange) | `--name` |
| `intro.txt` (pink) | `--file` |
| Variable names and "passed" (green) | `--var`, `--pass` |
| `====` section headings | `--heading` |
| Links | `--link` |
| Descriptions and small text | `--dim` |

**Important:** the dark colours are written **twice** (search for `--bg: #0d1926` and you'll find both). Change both blocks the same way, or dark mode will look different depending on how it was switched on. The light colours are the first `:root {` block at the very top of the style.

**Always dark:** to ignore the visitor's setting and always show the dark terminal, change the second line of the file to:

```html
<html lang="en" data-theme="dark">
```

### Font, size and width

| What | Search for |
| --- | --- |
| Font | `font-family: 'Source Code Pro'` (also change the Google Fonts `<link>` near the top if you switch fonts) |
| Text size on desktop | `font-size: 16px` |
| Text size on phones | `font-size: 14.5px` |
| Maximum page width | `max-width: 920px` |
| Width of the `[now]` / `[py]` column | `grid-template-columns: 7ch 1fr` (raise `7ch` if your dates are longer) |
| Width of the green variable-name column | `min-width: 11ch` |

### Typing speed

Near the bottom of the file. Numbers are milliseconds; smaller is faster.

| What | Search for |
| --- | --- |
| Time per typed letter | `38 + Math.random() * 34` |
| Pause before a command's output appears | `}, 260);` |
| Pause before the next command starts | `}, 420);` |
| Gap between each part of intro.txt appearing | `110 : 0` |

Visitors can always skip the animation with any key or the "skip animation" button, and people who have reduced-motion turned on see everything instantly.

---

## Gotchas

- **Apostrophes inside text.** Text is wrapped in single quotes, so an apostrophe inside it breaks the page. Write `'Surya\'s projects'` (backslash before the apostrophe) or avoid the apostrophe.
- **Commas.** Items in a list need commas between them, but a trailing comma after the last one is fine either way.
- **`+` at the end of HTML lines** in the work-experience and contact sections joins them together. If you add a line, keep the `+`.
