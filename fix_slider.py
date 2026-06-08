import re

# 1. FIX ICONS (Inject Material Symbols)
def inject_font(html):
    link = '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />'
    if 'Material+Symbols+Outlined' not in html:
        # insert before </head>
        html = html.replace('</head>', f'  {link}\n</head>')
    return html

with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index = f.read()
with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(inject_font(index))

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho = f.read()
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(inject_font(junho))

# 2. FIX CSS (.post-split duplication and broken layout)
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Completely remove old .post-split blocks
# Note: we need to handle media queries carefully or just wipe the blocks.
# Let's just wipe anything that looks like .post-split { ... }
css = re.sub(r"\.post-split\s*\{[^}]*\}", "", css)

# Wipe gallery-col and panel-actions-wrapper so we can append them cleanly
css = re.sub(r"\.gallery-col\s*\{[^}]*\}", "", css)
css = re.sub(r"\.gallery-col [^\{]+\s*\{[^}]*\}", "", css)
css = re.sub(r"\.panel-actions-wrapper\s*\{[^}]*\}", "", css)
css = re.sub(r"\.panel-actions-wrapper [^\{]+\s*\{[^}]*\}", "", css)
css = re.sub(r"\.abtn\s*\{[^}]*\}", "", css)

# Wipe .posts-horizontal-track media queries if any
# We'll just define the clean structure at the end of the file.

clean_css = """
/* ══ CLEAN POST STRUCTURE ══ */
.post-split {
  display: grid; grid-template-columns: minmax(320px, 1fr) minmax(320px, 1.2fr); gap: 40px;
  width: 100%; max-width: 1200px;
  margin: 0 auto; align-items: start;
}

.gallery-col {
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  background: transparent; border-radius: 24px; overflow: hidden; position: relative;
  width: 100%;
}
.gallery-col .ig-carousel {
  width: 100%; height: auto; position: relative; border-radius: 24px; overflow: hidden;
  box-shadow: 0 16px 40px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.4);
}
.gallery-col .ig-track {
  display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none;
}
.gallery-col .ig-track::-webkit-scrollbar { display: none; }
.gallery-col .ig-slide {
  min-width: 100%; display: flex; align-items: center; justify-content: center;
}
.gallery-col .ig-slide img {
  width: 100%; height: auto; object-fit: contain; display: block;
}

/* Action Buttons */
.panel-actions-wrapper {
  margin-top: 32px; padding-top: 24px; border-top: 1px solid rgba(0,0,0,0.06);
}
.panel-actions-wrapper .actions {
  display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap;
}
.panel-actions-wrapper .actions-left {
  display: flex; gap: 12px; flex: 1; flex-wrap: wrap;
}
.abtn {
  display: inline-flex; align-items: center; gap: 6px; justify-content: center;
  padding: 14px 24px; font-size: 14px; font-weight: 600; border-radius: 14px; cursor: pointer;
  background: #fff; color: var(--text); border: 1px solid var(--border);
}
.abtn.btn-ap { background: #007AFF; color: #fff; border: none; }
.abtn.btn-ap:active { transform: scale(0.98); }

@media(max-width: 900px) {
  .post-split { grid-template-columns: 1fr; gap: 24px; }
  .panel-actions-wrapper .actions { flex-direction: column; }
  .panel-actions-wrapper .actions-left { flex-direction: column; }
  .abtn { width: 100%; }
}
"""

css += clean_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed layout and icons!")
