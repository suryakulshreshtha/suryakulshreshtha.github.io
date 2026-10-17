# 🧭 GitHub Pages Index: `suryakulshreshtha`

> 📒 **Creator's reference.** One page that answers: *"Which websites do I have on `github.io`, which repo makes each one, and how do I change or add one?"*
> 📂 **File:** `GithubIOFileInstructions.md`. It lives in the repo `suryakulshreshtha.github.io` as a **secondary file**, next to that repo's own `README.md` (which stays the CV's readme and is never replaced by this file).
> ✏️ Edit this file whenever a site is added, changed or retired. Look for the 👉 **EDIT** markers.
> 🕒 **Last reviewed:** 2026-10-17

---

## 📑 Contents

| # | Section | What you will find |
|---|---------|--------------------|
| 1 | [🧠 The mental model](#-1-the-mental-model) | What `github.io` actually is |
| 2 | [🗺 Master index of sites](#-2-master-index-of-sites) | **The main table.** Every live site and its repo |
| 3 | [🎟 Slots and limits](#-3-slots-and-limits) | How many sites a free account can have |
| 4 | [📦 Per-site details](#-4-per-site-details) | Build, deploy and where to edit, per site |
| 5 | [➕ Add a new site](#-5-add-a-new-site) | Checklist |
| 6 | [➖ Retire a site](#-6-retire-a-site) | Checklist |
| 7 | [🌍 Custom domains](#-7-custom-domains) | GoDaddy and DNS records |
| 8 | [🩺 Health checks](#-8-health-checks) | Quick commands to see if things are up |
| 9 | [📓 Changelog](#-9-changelog) | What happened, and when |
| 10 | [🪦 Retired sites](#-10-retired-sites) | Graveyard, so old links are never a mystery |

---

## 🧠 1. The mental model

Every site has **two addresses**. Do not mix them up:

| 🏷 Thing | 🔗 Looks like | 👀 Who sees it | 💡 What it is |
|---------|--------------|----------------|---------------|
| 📦 **Repo** (the source) | `github.com/suryakulshreshtha/<repo>` | You (and anyone, if public) | The files, history and settings |
| 🌐 **`github.io` site** (the output) | `suryakulshreshtha.github.io/<repo>/` | The public | The finished website GitHub serves |

```
 ✍ you edit files  ──►  📦 repo on github.com  ──►  ⚙ build/publish  ──►  🌐 site on github.io
```

| 🧩 Kind of site | 🔗 Address | 📛 Repo name must be | 🔢 How many |
|----------------|-----------|---------------------|-------------|
| 👤 **User site** | `https://suryakulshreshtha.github.io/` | exactly `suryakulshreshtha.github.io` | **1** per account |
| 📁 **Project site** | `https://suryakulshreshtha.github.io/<repo>/` | anything | **1 per repo** |

---

## 🗺 2. Master index of sites

👉 **EDIT:** add one row per site. Keep the numbering. Move dead sites to [section 10](#-10-retired-sites).

| # | 🏷 Site | 🌐 Live address (`github.io`) | 📦 Repo | 🧩 Kind | 🟢 Status | 🔗 Custom domain | 📝 One-line purpose |
|---|---------|------------------------------|---------|---------|-----------|------------------|---------------------|
| 1 | 👤 **Profile / CV site** | [suryakulshreshtha.github.io](https://suryakulshreshtha.github.io/) | [`suryakulshreshtha.github.io`](https://github.com/suryakulshreshtha/suryakulshreshtha.github.io) | 👤 User site | 🟢 Live (checked 2026-10-17) | ❌ None | Professional profile page ("PO-QA SDET / Test Automation Engineer") |
| 2 | ✍ **Systemic Insolence** | [suryakulshreshtha.github.io/Systemic-Insolence](https://suryakulshreshtha.github.io/Systemic-Insolence/) | [`Systemic-Insolence`](https://github.com/suryakulshreshtha/Systemic-Insolence) | 📁 Project site | 🟢 Live (since 2026-10-17) | ⏳ Planned (GoDaddy) | Personal site: blog, photos, books, projects |
| 3 | 🆕 *(next site)* | | | | | | |

### 🚦 Status legend

| Icon | Meaning |
|------|---------|
| 🟢 | Live and working |
| 🟡 | Live but has a known problem (write it in the changelog) |
| 🔴 | Down or failing to publish |
| 🚧 | Being built, not public yet |
| 🪦 | Retired (move to section 10) |
| ❓ | Not checked yet |

---

## 🎟 3. Slots and limits

### 🔢 Slot counter

| 🎟 Slot | 📏 Allowed (free account) | ✅ Used | 🟩 Free |
|---------|---------------------------|--------|---------|
| 👤 User site (`<name>.github.io`) | 1 | **1** (#1 above) | **0** |
| 📁 Project sites | 1 per repo, public repos only | **1** (#2 above) | as many as you have public repos |
| 🔒 Pages on a *private* repo | ❌ not on the free plan | n/a | n/a |

### 📏 Platform limits (from GitHub's docs, checked 2026-10-17)

| 📐 Limit | 🔢 Value | 🧾 Note |
|----------|---------|---------|
| 💾 Published site size | **1 GB** max | Keep photos resized |
| 📶 Bandwidth | about **100 GB / month** | Soft cap |
| 🏗 Builds | about **10 / hour** | Soft cap; **does not apply** to builds run by a GitHub Actions workflow (site #2 uses one) |
| ⏱ Deploy time | **10 minutes** max | Then it times out |

📚 Source: GitHub docs, *GitHub Pages limits* and *About GitHub Pages*.

---

## 📦 4. Per-site details

👉 **EDIT:** copy one block per site. Fill what you know; leave ❓ for the rest.

### 👤 Site 1: Profile / CV (`suryakulshreshtha.github.io`)

| 🔑 Field | 📋 Value |
|----------|---------|
| 🌐 Address | https://suryakulshreshtha.github.io/ |
| 📦 Repo | https://github.com/suryakulshreshtha/suryakulshreshtha.github.io (public, branch `main`) |
| 🛠 Built with | Plain static HTML (`index.html`, `.nojekyll`, `README.md` seen in the repo root) |
| 🚀 Publish method | ❓ *to check:* repo **Settings → Pages → Source** (branch, or GitHub Actions) |
| 📅 Created | ❓ |
| ✏ How to edit | Change the files in the repo, commit to `main` |
| 🔗 Custom domain | ❌ none (no `CNAME` file seen) |
| 🗒 Notes | Uses the account's single user-site slot. The repo description reads "Github IO usage". |

### ✍ Site 2: Systemic Insolence

| 🔑 Field | 📋 Value |
|----------|---------|
| 🌐 Address | https://suryakulshreshtha.github.io/Systemic-Insolence/ |
| 📦 Repo | https://github.com/suryakulshreshtha/Systemic-Insolence (public, branch `main`) |
| 🛠 Built with | **Ruby on Rails 8.1 on Ruby 3.4.11, used as a static-site generator** (no server runs for visitors) |
| 🚀 Publish method | **GitHub Actions**: *Settings → Pages → Source → GitHub Actions* |
| ⚙ Workflows | 🚀 `Publish site` (`pages.yml`): on push to `main`, **every 6 hours (:17 past)**, and by hand · ✅ `Checks` (`ci.yml`): tests, security scan, style, trial build · 🔒 `Make Gemfile.lock` (`lockfile.yml`): manual helper · 🤖 Dependabot: weekly update PRs |
| 💻 Runner image | `ubuntu-24.04` (pinned on 2026-10-17 because `ubuntu-latest` moves to Ubuntu 26 on 2026-10-19) |
| 📅 Created | 2026-10-17 |
| ✏ How to edit | See **`UPDATING.md`** in that repo (posts, photos, books, projects, settings) |
| 🌍 Domain steps | See **`DOMAIN.md`** in that repo |
| 🛡 Security notes | See **`SECURITY.md`** in that repo |
| 🔑 Secrets | `GOOGLE_API_KEY` (only if the Drive photo sync is switched on; never store it in a file) |
| 🔗 Custom domain | ⏳ planned, not set yet |

#### 🗂 Where things live in Site 2

| 📁 Path | 🧾 What | ✍ You edit it to... |
|---------|---------|----------------------|
| `content/posts/` | Blog posts (`.md`) | 📝 publish writing |
| `content/pages/` | About, Now, About this site | 🙋 change standing pages |
| `content/projects/` | One `.yml` per project | 🧰 add project pages |
| `content/books.yml` | Books | 📚 add books |
| `public/media/photos/` | Photographs | 📷 add photos |
| `config/site.yml` | Name, tagline, links, data sources | ⚙ change site-wide settings |
| `.github/workflows/` | Publish and check automation | 🤖 (rarely) |

---

## ➕ 5. Add a new site

| ✅ | Step | 🧭 Where | 📝 Detail |
|----|------|----------|-----------|
| ☐ | 1⃣ Create the repo | github.com → **New repository** | **Public** (free Pages needs public). For a *user* site the name must be exactly `suryakulshreshtha.github.io`, but that slot is **already used** ⚠ |
| ☐ | 2⃣ Add the files | local folder, then `git push` | Plain HTML needs an `index.html` at the root |
| ☐ | 3⃣ Switch Pages on | Repo **Settings → Pages → Source** | 📄 Plain HTML: **Deploy from a branch**. 🏗 Generated site (like Rails): **GitHub Actions** |
| ☐ | 4⃣ Wait and open it | Repo **Actions** tab → then the address | Usually 1 to 4 minutes |
| ☐ | 5⃣ Check links | Open it at `…github.io/<repo>/` | Absolute links like `/css/x.css` break under a sub-path ⚠ |
| ☐ | 6⃣ Update this file | 👉 Section 2 row, Section 4 block, Section 3 counter, Section 9 changelog | ✍ |

📋 **Row template to copy into section 2:**

```markdown
| N | 🏷 **Name** | [suryakulshreshtha.github.io/repo](https://suryakulshreshtha.github.io/repo/) | [`repo`](https://github.com/suryakulshreshtha/repo) | 📁 Project site | 🟢 Live (since YYYY-MM-DD) | ❌ None | What it is |
```

---

## ➖ 6. Retire a site

| ✅ | Step | 📝 Detail |
|----|------|-----------|
| ☐ | 1⃣ Decide what happens to the address | A removed site returns GitHub's 404 page. Anything that linked to it breaks 🔗💥 |
| ☐ | 2⃣ Take it offline | Unpublish Pages in the repo's **Settings → Pages**, or delete the repo |
| ☐ | 3⃣ Keep the code? | 📦 **Archive** the repo (Settings → Danger Zone) instead of deleting, so history survives |
| ☐ | 4⃣ Remove any custom domain | Delete its DNS records at the registrar so nothing points at a dead site (security hygiene 🔐) |
| ☐ | 5⃣ Update this file | Move the row to **section 10**, free the slot in **section 3**, log it in **section 9** |

---

## 🌍 7. Custom domains

### 📇 Domain register

👉 **EDIT** when a domain is connected or removed.

| 🌐 Domain | 🏪 Registrar | 🎯 Points to (site #) | 📡 Record type | ✅ HTTPS enforced | 📅 Connected | 🟢 Status |
|-----------|-------------|-----------------------|---------------|-------------------|-------------|-----------|
| *(none yet)* | GoDaddy | ✍ Systemic Insolence (#2) planned | | | | ⏳ |

### 📡 DNS values for GitHub Pages (verified from GitHub's docs, 2026-10-17)

| 🧩 Type | 🏷 Name | 🎯 Value |
|---------|---------|---------|
| `CNAME` | `www` | `suryakulshreshtha.github.io` |
| `A` | `@` | `185.199.108.153` |
| `A` | `@` | `185.199.109.153` |
| `A` | `@` | `185.199.110.153` |
| `A` | `@` | `185.199.111.153` |
| `AAAA` (optional) | `@` | `2606:50c0:8000::153` · `2606:50c0:8001::153` · `2606:50c0:8002::153` · `2606:50c0:8003::153` |

### ⚠ Remember

| 💡 Rule | 🧾 Why |
|--------|--------|
| 🚫 No wildcard (`*`) DNS records | Can let someone else take over a subdomain |
| 🛑 Turn off GoDaddy **domain forwarding** for that domain | It fights with the GitHub records |
| 🔖 Set the domain in the repo's **Settings → Pages**, not with a `CNAME` file | A `CNAME` file does nothing when publishing from GitHub Actions |
| ⏳ DNS can take up to about 24 hours | HTTPS can lag the DNS check |
| 🧠 Before putting a custom domain on the **user site** (#1), read GitHub's docs on how it affects **project sites** | It can change where project sites are served ⚠ *(not verified here)* |
| 🔐 Verify the domain in your **account** Pages settings | Stops others from claiming it |

Full walkthrough: **`DOMAIN.md`** in the Systemic-Insolence repo.

---

## 🩺 8. Health checks

| 🎯 Question | 💻 Command / action |
|------------|---------------------|
| 🌐 Is site 1 up? | `curl -sI https://suryakulshreshtha.github.io/ \| head -1` → expect `HTTP/2 200` |
| 🌐 Is site 2 up? | `curl -sI https://suryakulshreshtha.github.io/Systemic-Insolence/ \| head -1` → expect `HTTP/2 200` |
| 🚀 Did the last publish work? | Repo → **Actions** → **Publish site** → green tick ✅ |
| 🛠 Why did a build fail? | Open the red run → click the red step → read the last lines |
| 📰 Is the feed alive? (site 2) | Open `…/Systemic-Insolence/feed.xml` |
| 🔁 Force a rebuild (site 2) | **Actions → Publish site → Run workflow** |
| 💤 Quiet repo warning | In a *public* repo GitHub switches off scheduled runs after **60 days** with no activity. Any commit wakes it |

---

## 📓 9. Changelog

👉 **EDIT:** newest first. One line per event. Future-you will thank you. 🙏

| 📅 Date | 🏷 Site | 🔔 Event | 📝 Detail |
|--------|---------|---------|-----------|
| 2026-10-17 | 🧭 Index | 📄 `GithubIOFileInstructions.md` created | Sites #1 and #2 recorded; stored beside the CV `README.md`, which was left untouched |
| 2026-10-17 | ✍ #2 | 🔒 `Gemfile.lock` added, runner pinned | Commit `471cc58`; `ubuntu-latest` → `ubuntu-24.04` |
| 2026-10-17 | ✍ #2 | 🚀 First publish succeeded | Commit `19ebcee`; live at the `github.io` address |
| 2026-10-17 | ✍ #2 | ⚠ `Checks` job failing | Suspected style-check step; being fixed. *Delete this line when green* ✅ |
| 2026-10-17 | ✍ #2 | 🆕 Repo created and first push | Rails static-site generator, GitHub Actions publish |

---

## 🪦 10. Retired sites

👉 **EDIT:** move rows here instead of deleting them, so an old link never becomes a mystery.

| # | 🏷 Site | 🌐 Old address | 📦 Repo (archived?) | 📅 Retired | 🧾 Why | ➡ Replaced by |
|---|---------|----------------|---------------------|-----------|--------|----------------|
| *(none yet)* | | | | | | |

---

## 🧾 How to keep this file honest

| 🔔 When this happens... | ✏ ...update this |
|------------------------|-------------------|
| 🆕 New Pages site | Sections 2, 3, 4, 9 |
| 🔗 Domain connected or removed | Sections 2, 7, 9 |
| 🔧 Build method or runner changes | Section 4, 9 |
| 🪦 Site retired | Sections 2 → 10, 3, 9 |
| 🔍 You check something marked ❓ | Replace the ❓ with the real value |

<!-- 🔐 Reminder: this repo is public. Never paste keys, tokens or passwords here. -->
