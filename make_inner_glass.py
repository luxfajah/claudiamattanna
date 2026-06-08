import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make info-progress translucent
css = re.sub(
    r'(\.info-progress\s*\{[^}]*background:\s*)var\(--surface\)',
    r'\1rgba(255, 255, 255, 0.4)',
    css
)

# Replace any other solid surfaces if needed.
# For example, ig-carousel placeholder is #e0e0e0. We can leave that.

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Inner elements updated!")
