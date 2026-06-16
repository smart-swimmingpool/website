# Smart Swimming Pool Website — Opencode Skill

## Project Overview

Static documentation site for [Smart Swimming Pool](https://smart-swimmingpool.com), built with **Hugo** + **Hextra theme**. Hosted on GitHub Pages. Supports **EN + DE** translations.

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
┌────────┴────────┐   ┌───────┴────────┐
│ Module Repos    │   │ Daily Cron     │
│ pool-controller │   │ 6:00 UTC       │
│ openhab-config  │   └────────────────┘
│ grafana-dash.   │
│ monitor         │
└─────────────────┘
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
- **Malformed YAML frontmatter** (e.g. `summary:Überwache` — missing space after colon): `extract_frontmatter` returns empty metadata but still strips frontmatter from body to avoid duplication
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

- English: `page.md` / `page.de.md`
- German pages mirror English structure
- `_index.md` → section landing, `_index.de.md` → German landing
- Frontmatter: YAML with `title`, `date`, `draft`, `tags`, etc.

### Hugo Config

- Theme: `hextra` (git submodule at `themes/hextra/`)
- Config: `hugo.yaml` (multilingual with EN + DE)
- Content: `content/` directory
- Static files: `static/` (images, CNAME, etc.)
