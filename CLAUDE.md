# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MkDocs documentation site for Wenzao University's USR (University Social Responsibility) program. The site provides information about multilingual medical translation services and educational support programs.

- **Theme**: Material for MkDocs
- **Language**: Traditional Chinese (zh-TW)
- **URL**: https://wzuusr.org/n (site is nested under /n/ path)

## Build Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Local development server (auto-reload)
mkdocs serve

# Build static site to site/ directory
mkdocs build
```

## Architecture

```
docs/                     # All content lives here
├── index.md              # Homepage
├── blog/posts/           # Activity blog posts (YYYY-*.md naming)
├── about/                # Program information
├── materials/            # Digital teaching materials
├── expo/                 # USR EXPO pages (zh/en)
├── assets/images/        # Images organized by category
│   ├── team/
│   ├── partners/
│   ├── awards/
│   ├── materials/
│   └── events/{year}/
└── stylesheets/extra.css # Custom styling (900+ lines)
```

## Key Configuration

- **mkdocs.yml**: Navigation structure, plugins (blog, search, tags, glightbox), theme settings
- **requirements.txt**: Python dependencies (mkdocs-material, glightbox, minify, etc.)
- **.github/workflows/deploy.yml**: Auto-deploys to GitHub Pages on push to master

## Deployment Notes

- Site builds to `_site/n/` (nested path structure)
- Root `index.html` redirects to original Wix site
- Social media redirects (fb/, ig/, yt/) are copied to root
- Git revision dates plugin requires full history (fetch-depth: 0 in CI)

## Adding Content

- **New pages**: Add .md file to `docs/`, update `nav` section in `mkdocs.yml`
- **Blog posts**: Create `docs/blog/posts/YYYY-title.md` with front matter
- **Images**: Place in appropriate `docs/assets/images/` subdirectory

## Custom Components (in extra.css)

The site uses custom CSS classes for:
- Hero sections with gradient backgrounds
- Card grids for team/partner displays
- Statistics counters
- Timeline layouts
- Image galleries with lightbox
