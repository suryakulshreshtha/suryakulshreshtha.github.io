# Site guide

Reference for setting up, editing and testing **https://suryakulshreshtha.github.io**.
Short version of everything is in the [README](../README.md).

- [How the page works](#how-the-page-works)
- [Putting the site online with GitHub Pages](#putting-the-site-online-with-github-pages)
- [Updating the site](#updating-the-site)
- [Where to edit things](#where-to-edit-things)
- [Look and feel](#look-and-feel)
- [Tests and CI](#tests-and-ci)
- [Preview image and screenshot](#preview-image-and-screenshot)
- [If something goes wrong](#if-something-goes-wrong)

---

## How the page works

Everything a visitor reads is written out as plain HTML inside `<main id="term">` in `index.html`.
That is what search engines, LinkedIn/Slack previews and browsers with JavaScript off receive.

The `<script>` at the bottom then hides it and replays it: it types each command, reveals each output, and ends on a blinking prompt.
It reads everything from the HTML, so **you never edit the script to change content**.

The animation is skipped (everything shows at once) when:

- the visitor presses any key, clicks the page, or clicks **skip animation**
- the visitor's device has *reduce motion* turned on
- the visitor is a crawler or link-preview bot

---

## Putting the site online with GitHub Pages

You only need a web browser and a GitHub account. Everything below is done on github.com.
The site lives at **https://suryakulshreshtha.github.io**.

### Step 1 — Create the repository

1. Sign in to github.com.
2. In the top-right corner of any page, click the **+** icon, then click **New repository**.
3. **Owner:** pick your own account, `suryakulshreshtha`.
4. **Repository name:** type exactly:
   ```
   suryakulshreshtha.github.io
   ```
   The name must be your username followed by `.github.io`, all in lowercase. Any other name gives you a different address (`suryakulshreshtha.github.io/<name>`) instead of the main one.
5. **Description:** optional, e.g. `Personal website`.
6. **Visibility:** choose **Public**. On a free account, Pages only works on public repositories. (Even on paid plans, the site itself is always public.)
7. Turn the **Add README** switch **On**. This creates the `main` branch straight away, which Step 3 needs.
8. Click **Create repository**.

### Step 2 — Add the files

1. On the repository's main page, click **Add file**, then **Upload files**.
2. Drag in the repository's files, keeping their folders (`tests/`, `scripts/`, `docs/`, `.github/workflows/`).
   - `index.html` must sit at the top level, not inside a folder. Pages looks for a file called exactly `index.html` there.
   - Folders whose names start with a dot (`.github`) can be hard to drag in. Using git (see [Updating the site](#updating-the-site)) avoids that.
3. In the commit message box, type something like `Add website`.
4. Leave **Commit directly to the main branch** selected and click **Commit changes**.

### Step 3 — Turn on GitHub Pages

1. On the repository page, click the **Settings** tab. If you can't see it, click the **···** menu at the end of the tab row, then **Settings**.
2. In the left sidebar, under **Code and automation**, click **Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Under **Branch**, pick **main**, then **/ (root)** in the folder dropdown.
5. Click **Save**.

### Step 4 — Visit the site

1. Wait a few minutes. Publishing can take **up to 10 minutes**.
2. Go back to **Settings → Pages**. When it's ready, the top shows your address with a **Visit site** button.

The **Actions** tab shows the publishing job (`pages build and deployment`): yellow dot = running, green tick = live, red cross = failed (click it to see why).
The same tab also shows this repo's own test workflows, **site tests** and **link rot**.

### Step 5 — Skip GitHub's page builder (already done)

By default GitHub runs sites through Jekyll. This site is plain HTML and doesn't need it, so the repo contains an empty file called `.nojekyll`.
Keep it: without it, publishing is slower and Markdown files may be turned into pages.

---

## Updating the site

**Quick edit in the browser:**

1. On the repository page, click `index.html`.
2. Click the **pencil icon** (Edit this file).
3. Make your change (see [Where to edit things](#where-to-edit-things)).
4. Click **Commit changes**, add a short message, and click **Commit changes** again.

**With git from a terminal:**

```bash
git clone https://github.com/suryakulshreshtha/suryakulshreshtha.github.io.git
cd suryakulshreshtha.github.io
# ...edit index.html...
pytest                      # optional but recommended, see Tests and CI
git add .
git commit -m "Update site"
git push
```

Every push to `main` republishes the site (allow up to 10 minutes) and runs the test suite.
If you still see the old version, hard refresh: **Ctrl+Shift+R** (Windows/Linux) or **Cmd+Shift+R** (Mac).

**Preview before pushing:** run `python -m http.server 8000` in the repo folder and open http://localhost:8000.
Double-clicking `index.html` also works.

---

## Where to edit things

Line numbers drift, so each item gives you text to **search for** (Ctrl+F / Cmd+F) in `index.html`.

Text inside the HTML follows HTML rules: write `&amp;` for `&`, and `&lt;` for `<`. Apostrophes and quotes are fine.

### The prompt (`Callsign@Anti-Errorist`)

It appears once per command. Use **find and replace** on `Callsign@Anti-Errorist` to change them all.
Also change it in `scripts/og-card.html` if you want the preview card to match.

### Browser tab title, search description and link previews

All in the `<head>` at the top of the file. Keep these in step when you change your role:

| What | Search for |
| --- | --- |
| Tab title / search result title | `<title>` |
| Search result description | `name="description"` |
| LinkedIn / Slack / WhatsApp preview | `og:title`, `og:description`, `og:image:alt` |
| X (Twitter) preview | `twitter:title`, `twitter:description`, `twitter:image:alt` |
| Structured data for Google | `application/ld+json` (`jobTitle`, `worksFor`, `sameAs`) |

The tests require the title to start with `Surya Kulshreshtha`, contain `SDET`, and stay under 66 characters, and the description to be 50–160 characters.

### Tab icon (🧪)

Search for `rel="icon"`. Swap the emoji inside `<text ...>🧪</text>` for any other single emoji.

### The commands and their output

Each command is one block:

```html
<div class="block">
  <div class="prompt">…<span class="cmd">uname -a</span></div>
  <p class="out strong">PO-QA sdet / test automation engineer — …</p>
</div>
```

- The text inside `<span class="cmd">` is what gets typed.
- Everything after the prompt line is the output. Each top-level element is revealed one after another.
- To add a command, copy a whole `<div class="block">…</div>` and change it. To remove one, delete the whole block.
- The one-line bio is the `uname -a` output. Your name is the `<h1>` under `grep "root"`; keep exactly one `<h1>`.

### Everything printed by `cat intro.txt`

All inside the block whose command is `cat intro.txt`.

**Section headings** look like this (the `====` lines are decoration hidden from screen readers):

```html
<h2 class="section"><span aria-hidden="true">================
</span>TECH STACK<span aria-hidden="true">
================</span></h2>
```

Keep the line breaks exactly where they are. If you rename or add a section, update `SECTIONS` in `tests/test_crawlable.py`.

**Root variables and tech stack** are the green `name = [...]` lines. Each line is one `dt`/`dd` pair:

```html
<dt class="k">testing</dt><dd class="v">= ['Playwright', 'Pytest', 'API &amp; DB testing', 'Postman']</dd>
```

Add a skill by adding `'NewThing'` inside the brackets. Add a line by copying a pair.

**Work experience**, one `<li>` per job:

```html
<li class="row tagged"><span class="tag">[now]</span><span><a href="https://www.protiviti.com" target="_blank" rel="noopener">Protiviti</a></span></li>
```

- Replace `[now]` / `[past]` with dates, e.g. `[2024–now]`. Tags longer than 6 characters need a wider column (see [Font, size and width](#font-size-and-width)).
- To add a job title, put it before the link: `<span><b>SDET</b>, <a …>Protiviti</a></span>`.

**Projects**, one `<li>` per repo, in the list with `class="rows projects"`:

```html
<li class="row tagged"><span class="tag lang">[py]</span><span><a class="strong" href="https://github.com/suryakulshreshtha/RepoName" target="_blank" rel="noopener">RepoName</a> <span class="c-dim">short description</span></span></li>
```

The repo name in the link must match GitHub exactly; the weekly **link rot** check fails on a typo.

**Blog and contact** are the `<p class="rows">` lines after the `BLOG` and `CONTACT` headings.

**A brand-new section**: copy one `<h2 class="section">…</h2>` plus the list under it, then add its title to `SECTIONS` in `tests/test_crawlable.py`.

### Links

Every link that opens in a new tab needs `target="_blank" rel="noopener"`. The tests enforce it.

### The `pytest -q` result at the end

This is real: it must equal the number of tests in `tests/`. Search for `id="test-count"` and `id="test-dots"`.
When you add or remove a test, run `pytest --collect-only -q`, then set the count to the number before `/` in the last line and make the dots the same length.
`tests/test_honesty.py` fails CI if they drift.

---

## Look and feel

All styling is in the `<style>` block at the top of `index.html`.

### Colours

The site follows the visitor's device setting: dark mode shows the navy terminal, light mode a pale version.

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

- The dark colours are written **twice** (search for `--bg: #0d1926` to find both). Change both blocks the same way.
- The light colours are the first `:root {` block. Light `--name` and `--dim` were darkened slightly (`#a54f00`, `#5f6874`) so text meets the WCAG AA 4.5:1 contrast minimum. The accessibility test will flag any colour that drops below it.
- **Always dark:** change the second line of the file to `<html lang="en" data-theme="dark">`.

### Font, size and width

| What | Search for |
| --- | --- |
| Font | `font-family: 'Source Code Pro'` (also change the Google Fonts `<link>` near the top if you switch fonts) |
| Text size on desktop | `font-size: 16px` |
| Text size on phones | `font-size: 14.5px` |
| Maximum page width | `max-width: 920px` |
| Width of the `[now]` / `[py]` column | `grid-template-columns: 7ch 1fr` (raise `7ch` for longer dates) |
| Width of the green variable-name column | `min-width: 11ch` |

### Typing speed

In the `<script>` near the bottom. Numbers are milliseconds; smaller is faster.

| What | Search for |
| --- | --- |
| Delay before the first command | `run(0); }, 450` |
| Time per typed letter | `38 + Math.random() * 34` |
| Pause before a command's output appears | `}, 260);` |
| Pause before the next command starts | `run(i + 1); }, 420` |
| Gap between each part of intro.txt appearing | `110 : 0` |

---

## Tests and CI

```bash
pip install -r requirements-dev.txt
python -m playwright install chromium
pytest
```

- **`pytest`** runs the main suite. It serves the repo on a random localhost port and replaces Google Fonts and the badge with stubs, so it runs offline and gives the same result every time.
- **`pytest -m external`** visits every outside link on the page (GitHub repos, LinkedIn, Protiviti, NICSI, your blog). LinkedIn answers bots with status 999, which counts as alive.
- **`SITE_URL=https://suryakulshreshtha.github.io pytest`** runs the same suite against the live site, without stubs.
- **Debug a failure visually:** `pytest --headed --slowmo 300 -k skip`, or `pytest --tracing on` and open the trace with `playwright show-trace test-results/…/trace.zip`.

`tests/pages.py` is a small page object (`Terminal`) the tests share: `open()`, `skip_animation()`, `finished()`, plus locators for blocks, commands, the skip button and the test count.

### Workflows

| Workflow | When | What |
| --- | --- | --- |
| `.github/workflows/ci.yml` (**site tests**) | every push to `main`, every pull request, manual | full suite; on failure uploads Playwright traces and screenshots as an artifact for 7 days |
| `.github/workflows/links.yml` (**link rot**) | Mondays 04:17 UTC, manual | `pytest -m external` |

The external check is kept out of the main workflow so a slow third-party site can't turn the site's badge red.
Both workflows only have read access to the repo and never change anything.

---

## Preview image and screenshot

`og.png` (the card shown when the link is shared) and `docs/screenshot.png` (used in the README) are generated:

```bash
python scripts/capture.py
```

Edit the card's text and colours in `scripts/og-card.html`. Keep it 1200×630; the tests check that size.
Re-run the script after visible changes, and commit both images.
Link previews are cached by each platform; LinkedIn's [Post Inspector](https://www.linkedin.com/post-inspector/) refreshes its copy.

---

## If something goes wrong

| What you see | What to check |
| --- | --- |
| A GitHub **404** page | The repository name is exactly `suryakulshreshtha.github.io`; `index.html` is at the top level and lowercase; **Settings → Pages** shows branch `main` and folder `/ (root)`. |
| Nothing has changed after 10 minutes | **Actions** tab → `pages build and deployment`. If it has a red cross, open it, read the error, click **Re-run jobs**. |
| Still not publishing | Commits must come from an account with admin rights on the repo and a **verified email** (**Settings → Emails**). |
| **site tests** is red | Open the run and read the first failing test's message. Common causes: test count not updated, a colour below contrast, a heading renamed without updating `SECTIONS`, a new-tab link missing `rel="noopener"`. Traces are under the run's **Artifacts**. |
| **link rot** is red | One outside link is broken or a repo was renamed. The failing test's name is the URL. |
| Page shows but doesn't animate | Open the browser console (**F12 → Console**). A script error makes the page show everything without animating rather than stay blank. |
| Your README shows instead of the site | `index.html` is missing from the top level or misnamed. |
