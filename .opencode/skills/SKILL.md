# Smart Swimming Pool Website — Opencode Skill

## Project Overview

Static documentation site for [Smart Swimming Pool](https://smart-swimmingpool.com),
built with **Hugo** + **Hextra theme**. Hosted on GitHub Pages.
Supports **EN + DE** translations.

## Architecture

```
┌──────────────────────────────────────────────────┐
│                   Website Repo                    │
│  ┌─────────────┐  ┌────────────┐  ┌───────────┐  │
│  │ content/docs/│  │ grabrepos  │  │ hugo.yaml │  │
│  │ (canonical)  │  │ .py        │  │ (config)  │  │
│  └──────┬───────┘  └─────┬──────┘  └───────────┘  │
│         │                │                         │
│         ▼                ▼                         │
│  ┌─────────────────────────────────────────────┐   │
│  │  GitHub Actions (CI) ─► Hugo ─► GitHub Pages│   │
│  └─────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────┘
        ▲                    ▲
        │ module docs        │ repository_dispatch
        │ (cloned/fetched)   │ (doc_update)
┌───────┴────────┐   ┌──────┴─────────┐
│ Module Repos   │   │ Daily Cron     │
│ pool-controller│   │ 6:00 UTC       │
│ openhab-config │   └────────────────┘
│ grafana-dash.  │
│ monitor        │
└────────────────┘
```

## Module Documentation Workflow

Four external module repos provide documentation that is merged into the website via `grabrepos.py`:

| Repo | Docs Directory |
|------|---------------|
| `smart-swimmingpool/pool-controller` | `content/docs/pool-controller/` |
| `smart-swimmingpool/openhab-config`  | `content/docs/openhab-configuration/` |
| `smart-swimmingpool/grafana-dashboard` | `content/docs/grafana-dashboard/` |
| `smart-swimmingpool/monitor` | `content/docs/pool-monitor/` |

### How `grabrepos.py` works

1. **Reads `multiversion.yml`** — finds enabled repos with file patterns
2. **Clones/fetches each repo** into `temp/<name>/`
3. **Scans for matching files** (default: `docs/**/*.md`)
4. **For each file**:
    - Extracts frontmatter (YAML) with `extract_frontmatter()`
    - Checks for `##` headings via `split_by_headings()`
    - **`_index.md` files** are always written (even without `##` headings)
    - **Other files** are skipped if they have no `##` sections
5. **Writes output** to `content/docs/<reponame>/` with combined frontmatter (source info + preserved metadata)

### Key Files

| File | Purpose |
|------|---------|
| `grabrepos.py` | Python script that clones module repos and generates docs |
| `multiversion.yml` | Config: which repos, file patterns, cleanup settings |
| `content/docs/_index.md` | Docs landing page with module listing |
| `docs/trigger-website-rebuild.md` | Guide for module maintainers (at GitHub level, not Hugo content) |

### Common Tasks for AI Agents

```bash
# Regenerate all module docs
python grabrepos.py

# Regenerate with clean temp directory first
# (set 'clean: true' in multiversion.yml)

# Verify build
hugo

# Dev server
hugo server -D
```

### Known `grabrepos.py` Edge Cases

- **No `##` headings in `_index.md`**: Safe — always written regardless
- **Malformed YAML frontmatter** (e.g. `summary:Überwache` — missing space after colon):
  `extract_frontmatter` returns empty metadata but still strips frontmatter from body
  to avoid duplication
- **Internal documents**: Skipped if frontmatter has `noindex: true` + `private: true`

### Build Triggers

| Trigger | Method |
|---------|--------|
| Push to `main` | GitHub Actions CI |
| Daily 6:00 UTC | Cron in `deploy-hugo.yml` |
| Module doc update | `repository_dispatch` with type `doc_update` |
| Manual | GitHub Actions → "Run workflow" |

### Module Docs are Git-Ignored

The generated directories are in `.gitignore` — they are never committed:
```
content/docs/pool-controller/
content/docs/openhab-configuration/
content/docs/grafana-dashboard/
content/docs/pool-monitor/
```

## Development

### Prerequisites

- Hugo (extended) v0.162.1+
- Python 3.x + `pip install -r requirements.txt`
- Git with submodule support

### Translation Pattern

This project uses Hugo's **filename-suffix** translation system (`hugo.yaml` has `languages: [en, de]` with no custom `contentDir`).

**Core rule:** German translations always use the `.de.md` suffix in the **same directory**
as the English original. Never place German files in a `content/de/` subdirectory — Hugo
would treat them as default-language content at a `/de/` path, breaking the sidebar,
language switcher, and URL structure.

#### File Naming Conventions

| English | German | Description |
|---------|--------|-------------|
| `_index.md` | `_index.de.md` | Section landing page (directory index) |
| `page.md` | `page.de.md` | Regular content page |
| `code-of-conduct.md` | `code-of-conduct.de.md` | Root-level standalone page |
| `smart-swimming-pool-project.md` | `projekt-smart-swimmingpool-einleitung.de.md` | Blog post (independent filenames per language) |

#### Rules per Content Type

**Section landing pages (`_index.md`):**
- English: `content/docs/<section>/_index.md`
- German: `content/docs/<section>/_index.de.md` (same directory)
- Both share frontmatter fields like `title`, `weight`, `tags` — each in its own language
- Example: `content/docs/architecture/_index.md` + `content/docs/architecture/_index.de.md`

**Regular doc pages:**
- Place the German `.de.md` file right next to the English `.md` file
- Never use `content/de/docs/...` paths
- This applies across all doc sections: `getting-started/`, `faq/`, `quickstart/`, `migration/`, `troubleshooting/`, etc.

**Root-level pages (`content/`):**
- Same pattern: `content/privacy.md` + `content/privacy.de.md`
- Examples: `code-of-conduct`, `license`, `privacy`

**Blog posts:**
- English: `content/blog/<english-slug>.md`
- German: `content/blog/<german-slug>.de.md`
- Filenames are **independent per language** (not just a suffix swap) — each uses a slug in its own language
- ⚠️ Because the base names differ, Hugo will **not** auto-link them as translations. Add a
  shared `translationKey` in both files' frontmatter (see Frontmatter Rules below)
- Example: `content/blog/smart-swimming-pool-project.md` and `content/blog/projekt-smart-swimmingpool-einleitung.de.md`
  — these are paired via `translationKey: "smart-pool-project"`, not by filename

**Generated docs (via `grabrepos.py`):**
- The script copies all `_index.md` and `_index.de.md` files from source module repos — it already
  handles German landing pages if they exist in the source
- Add German `_index.de.md` files directly in the **source module repo** (`smart-swimmingpool/pool-controller`,
  `smart-swimmingpool/openhab-config`, etc.), not in this repo
- The generated directories (`content/docs/pool-controller/`, etc.) are **gitignored** — manual files
  placed there will never be committed. If an override in this repo is absolutely required, modify
  `.gitignore` to allow specific `.de.md` files first

#### Frontmatter Rules

- **Required:** `title` in the respective language, `date`
- **Optional:** `draft`, `tags`, `weight`, `description`
- **Cross-linking:** Use Hugo's `relref` shortcode with the `lang` parameter for cross-language links.
  For pages where English and German share the same logical path (section indexes, same-slug pages):
  ```markdown
  {{< relref path="docs/getting-started" lang="en" >}}
  {{< relref path="docs/getting-started" lang="de" >}}
  ```
- Do **not** use `content/de/` paths in `relref` — always reference the canonical path with `lang="de"`
- ⚠️ **For independent filenames (blog posts):** The `path` must point to the actual file path
  in the target language, because the English and German slugs differ:
  ```markdown
  {{< relref path="/blog/projekt-smart-swimmingpool-einleitung" lang="de" >}}
  {{< relref path="/blog/smart-swimming-pool-project" lang="en" >}}
  ```
- **Translation linking for independent filenames:** When English and German files use different
  base names (e.g. blog posts with language-specific slugs), Hugo does **not** auto-link them
  as translations. Add a shared `translationKey` frontmatter field in **both** files:
  ```yaml
  # English: content/blog/smart-swimming-pool-project.md
  title: "Smart Swimming Pool Project"
  translationKey: "smart-pool-project"
  ---
  # German: content/blog/projekt-smart-swimmingpool-einleitung.de.md
  title: "Projekt Smart Swimmingpool – Einleitung"
  translationKey: "smart-pool-project"
  ```

#### Validation Checklist

When adding or reviewing multilingual content:

- [ ] German file has `.de.md` suffix (not in `content/de/` subdirectory)
- [ ] Both `_index.md` and `_index.de.md` exist in the same directory
- [ ] Frontmatter `title` is translated, not copied from English
- [ ] Cross-language `relref` links use the `lang` parameter
- [ ] No duplicate content at `content/de/...` paths
- [ ] Independent filename pairs (blog posts) share a `translationKey` in frontmatter

### Hugo Config

- Theme: `hextra` (git submodule at `themes/hextra/`)
- Config: `hugo.yaml` (multilingual with EN + DE)
- Content: `content/` directory
- Static files: `static/` (images, CNAME, etc.)
