import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fonts
# Remove google fonts imports
css = re.sub(r"@import url\('https://fonts.googleapis.com/css2\?family=[^']+'\);\n?", '', css)

# Update font variables
css = re.sub(r"--font-main:\s*'Inter',\s*sans-serif;", '--font-main: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;', css)
css = re.sub(r"--font-head:\s*('Playfair Display'|'Fraunces'|'Canela')[^;]*;", '--font-head: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;', css)

# Also catch explicit font-family assignments
css = re.sub(r"font-family:\s*('Canela'|'Fraunces'|'Playfair Display')[^;]*;", "font-family: var(--font-head);", css)
css = re.sub(r"font-family:\s*'Inter'[^;]*;", "font-family: var(--font-main);", css)
css = re.sub(r"font-family:\s*sans-serif;", "font-family: var(--font-main);", css)
css = re.sub(r"font-style:\s*italic;", "font-style: normal;", css) # Apple rarely uses italic headers

# 2. Colors
# Update brand colors to Apple System Blue
css = re.sub(r"--rose:\s*#[0-9a-fA-F]+;", "--rose: #007AFF;", css)
css = re.sub(r"--wine:\s*#[0-9a-fA-F]+;", "--wine: #0056B3;", css)

# 3. Glassmorphism Vibrancy & Squircles
# Thick material
vibrancy = "backdrop-filter: blur(40px) saturate(200%); -webkit-backdrop-filter: blur(40px) saturate(200%);"
soft_shadow = "box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);"

# .info-panel
css = re.sub(
    r"(\.info-panel\s*\{[^}]*background:\s*)rgba\(255,\s*255,\s*255,\s*[0-9.]+\)([^}]*)\}",
    r"\1rgba(255, 255, 255, 0.65)\2}",
    css
)
css = re.sub(r"backdrop-filter:\s*blur\(24px\)[^;]*;", vibrancy, css)
css = re.sub(r"border-radius:\s*28px;", "border-radius: 32px;", css)
css = re.sub(r"box-shadow:\s*0 30px 90px rgba\([^)]+\);", soft_shadow, css)

# inner blocks (.igp, .post-panel, .ig-phone, .lb-right)
for sel in ['.igp', '.post-panel', '.ig-phone', '.lb-right']:
    # Replace background and blur
    pass

# Let's do a blanket replacement for blur(24px) saturate(1.2)
css = css.replace("backdrop-filter: blur(24px) saturate(1.2);", vibrancy)
css = css.replace("-webkit-backdrop-filter: blur(24px) saturate(1.2);", vibrancy)
css = css.replace("backdrop-filter: blur(30px) saturate(1.2);", vibrancy)
css = css.replace("-webkit-backdrop-filter: blur(30px) saturate(1.2);", vibrancy)

# Set their border-radius to 24px (was usually radius-lg which might be 20px)
css = re.sub(r"--radius-lg:\s*20px;", "--radius-lg: 24px;", css)
css = re.sub(r"--radius:\s*12px;", "--radius: 16px;", css)

# 4. Buttons
# Replace button radius
css = css.replace("border-radius: 100px;", "border-radius: 14px;") # modal-btn
css = css.replace("border-radius:var(--radius-pill);", "border-radius: 14px;") # dl-card, download-btn
css = re.sub(r"(--radius-pill:\s*)100px;", r"\1 14px;", css)

# Adjust title font weights
css = re.sub(r"(\.info-title\s*\{[^}]*)font-weight:\s*300;", r"\1font-weight: 700; letter-spacing: -0.02em;", css)
css = re.sub(r"(\.footer-title\s*\{[^}]*)font-weight:\s*300;", r"\1font-weight: 700; letter-spacing: -0.02em;", css)
css = re.sub(r"(\.hero-title\s*\{[^}]*)font-weight:\s*300;", r"\1font-weight: 700; letter-spacing: -0.02em;", css)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index = f.read()
index = re.sub(r"@import url\('https://fonts.googleapis.com/css2\?family=[^']+'\);\n?", '', index)
index = re.sub(r"--font-main:\s*'Inter',\s*sans-serif;", '--font-main: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;', index)
index = re.sub(r"--font-head:\s*('Playfair Display'|'Fraunces'|'Canela')[^;]*;", '--font-head: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;', index)
index = re.sub(r"font-family:\s*('Canela'|'Fraunces'|'Playfair Display')[^;]*;", "font-family: var(--font-head);", index)
index = re.sub(r"font-family:\s*'Inter'[^;]*;", "font-family: var(--font-main);", index)
index = index.replace("border-radius: 100px;", "border-radius: 14px;")
with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

print("iOS styles applied!")
