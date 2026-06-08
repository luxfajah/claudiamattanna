import re

# 1. Update css panels
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace info-panel
css = re.sub(
    r'(\.info-panel\s*\{[^}]*background:\s*)rgba\(255,\s*255,\s*255,\s*0\.95\)',
    r'\1rgba(255, 255, 255, 0.65)',
    css
)

# igp
css = re.sub(
    r'(\.igp\s*\{[^}]*background:\s*)var\(--white\)',
    r'\1rgba(255, 255, 255, 0.65);\n  backdrop-filter: blur(24px) saturate(1.2);\n  -webkit-backdrop-filter: blur(24px) saturate(1.2)',
    css
)

# post-panel
css = re.sub(
    r'(\.post-panel\s*\{[^}]*background:\s*)var\(--white\)',
    r'\1rgba(255, 255, 255, 0.65);\n  backdrop-filter: blur(24px) saturate(1.2);\n  -webkit-backdrop-filter: blur(24px) saturate(1.2)',
    css
)

# ig-phone
css = re.sub(
    r'(\.ig-phone\s*\{[^}]*background:\s*)var\(--white\)',
    r'\1rgba(255, 255, 255, 0.65);\n  backdrop-filter: blur(24px) saturate(1.2);\n  -webkit-backdrop-filter: blur(24px) saturate(1.2)',
    css
)

# lb-right
css = re.sub(
    r'(\.lb-right\s*\{[^}]*background:\s*)#fff',
    r'\1rgba(255, 255, 255, 0.85);\n  backdrop-filter: blur(30px) saturate(1.2);\n  -webkit-backdrop-filter: blur(30px) saturate(1.2)',
    css
)

# login-box (in index.html css or junho.css? login-box is inline or in html? wait it's in index.html)
# Let's check index.html for login-box
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Make body have the background
index_html = index_html.replace(
    ".hero-bg { background:",
    "body { background: var(--current-bg) center/cover fixed no-repeat !important; }\n        .hero-bg { background:"
)

with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Update junho.html for body background
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho_html = f.read()

junho_html = junho_html.replace(
    ".hero-bg { background:",
    "body { background: var(--current-bg) center/cover fixed no-repeat !important; }\n        .hero-bg { background:"
)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(junho_html)

# Save css
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Glass applied globally!")
