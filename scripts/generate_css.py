#!/usr/bin/env python3
"""Generate public/css/*.css from palette.json. Deterministic — no inputs
besides palette.json, no hardcoded values below (all derived).

Usage: python3 scripts/generate_css.py  (run from repo root, commit output)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def darken(hex_color, pct):
    hex_color = hex_color.lstrip("#")
    f = max(0.0, 1.0 - pct / 100.0)
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(int(r * f), int(g * f), int(b * f))


def rgba(hex_color, alpha):
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return f"rgba({r}, {g}, {b}, {alpha})"


def main():
    with open(os.path.join(ROOT, "palette.json")) as f:
        pal = json.load(f)
    brand = pal["brand"]
    hover = darken(brand, pal.get("brand_hover_darken_pct", 12))
    selection = rgba(brand, pal.get("selection_alpha", 0.22))

    # Surface-level only: remap link/accent tokens + native control accents.
    # Backgrounds, sidebar, navbar, typography, spacing: untouched (stock).
    css = f"""/* Synotech surface theme — GENERATED from palette.json, do not hand-edit.
 * Only link/accent tokens are remapped; everything else stays stock. */
:root {{
  --link-color: {brand};
  --link-hover-color: {hover};
  --brand-color: {brand};
  --brand-hover-color: {hover};
}}

a, .link, .link-color {{
  color: var(--link-color);
}}
a:hover, .link:hover {{
  color: var(--link-hover-color);
}}

input[type="checkbox"], input[type="radio"] {{
  accent-color: var(--brand-color);
}}

:focus-visible {{
  outline-color: var(--brand-color);
}}

::selection {{
  background: {selection};
}}

.btn-brand, .btn-primary.btn-brand {{
  background-color: var(--brand-color);
  border-color: var(--brand-color);
}}
.btn-brand:hover {{
  background-color: var(--brand-hover-color);
  border-color: var(--brand-hover-color);
}}
"""
    for name in ("synotech-desk.css", "synotech-web.css"):
        path = os.path.join(ROOT, "synotech_theme", "public", "css", name)
        with open(path, "w") as f:
            f.write(css)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
