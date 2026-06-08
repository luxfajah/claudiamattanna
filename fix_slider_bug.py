import re

# 1. Fix HTML structure for the Lightbox click event
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the onclick from ig-carousel and move it to ig-track
html = re.sub(
    r'<div class="ig-carousel" style="cursor:pointer" onclick="openLightbox\(\'(\d+)\'\)">\s*<div class="ig-track" id="itrack-\1">',
    r'<div class="ig-carousel">\n          <div class="ig-track" id="itrack-\1" style="cursor:pointer" onclick="openLightbox(\'\1\')">',
    html
)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix CSS height for the images
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r"\.ig-slide\s*\{\s*min-width:\s*100%;\s*position:\s*relative;\s*display:\s*flex;\s*align-items:\s*center;\s*justify-content:\s*center;\s*\}",
    """
.ig-slide {
  min-width: 100%; position: relative; height: 100%;
  display: flex; align-items: center; justify-content: center;
}
""",
    css
)

# Ensure image takes full height to be contained properly
css = re.sub(
    r"\.ig-slide img\s*\{\s*width:\s*100%;\s*height:\s*auto;\s*display:\s*block;\s*object-fit:\s*contain;\s*\}",
    """
.ig-slide img {
  width: 100%; height: 100%; display: block; object-fit: contain;
}
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Slider and Lightbox fixed!")
