import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the primary button half width and apply Grid order to rearrange visually
css = re.sub(
    r"\.abtn\.btn-ap\s*\{\s*grid-column:\s*1\s*/\s*-1;",
    ".abtn.btn-ap {",
    css
)

css += """
/* Grid Rearrangement for 2x2 */
.abtn.btn-ap { order: 1; grid-column: auto; }
.abtn.btn-lt { order: 2; } /* Revisar */
.abtn.btn-rj { order: 3; } /* Reprovar */
.abtn.btn-cm { order: 4; } /* Comentários */
"""

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Fix the 3rd lightbox click event
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<div class="ig-carousel" style="cursor:pointer" onclick="openLightbox\(\'3\'\)">\s*<div class="ig-track" id="itrack-3">',
    r'<div class="ig-carousel">\n          <div class="ig-track" id="itrack-3" style="cursor:pointer" onclick="openLightbox(\'3\')">',
    html
)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Buttons rearranged and 3rd lightbox fixed!")
