# Synotech Theme

Surface-level brand theme for Frappe/ERPNext. Remaps **link/accent tokens
only** (links, hovers, checkbox/radio accents, focus rings, text selection,
plus an opt-in `.btn-brand` class) to the Synotech brand color. Backgrounds,
sidebar, navbar, typography, spacing: stock.

## The rule

`palette.json` is the only place a color value exists. CSS is generated:

```sh
python3 scripts/generate_css.py   # writes synotech_theme/public/css/*.css
```

Edit the palette, regenerate, commit both. No hostnames, secrets, or
per-site values anywhere in this repo — one theme serves the whole fleet.

## Install

Via the ERP image (`apps.json` row) — auto-installed on every site by the
`create-site` loop. Hooks used: `app_include_css` (Desk),
`web_include_css` (portal/login). No JS, no doctypes, no patches.
