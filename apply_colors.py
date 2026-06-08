import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Introduce --accent if not exists
if "--accent:" not in css:
    css = re.sub(
        r":root\s*\{",
        ":root {\n  --accent: #B8975A;\n",
        css
    )

# Replace `#007AFF` (which was the old rose/highlight color) with `var(--accent)`
css = css.replace('#007AFF', 'var(--accent)')
css = css.replace('var(--rose)', 'var(--accent)')

# Ensure font color is only var(--text)
# We can find `color: #000;`, `color: #333;`, `color: var(--muted);` and change to `color: var(--text);`
# But we might want `opacity: 0.7` instead of different colors for "muted" text.
css = re.sub(r"color:\s*#000;?", "color: var(--text);", css)
css = re.sub(r"color:\s*#333;?", "color: var(--text);", css)
css = re.sub(r"color:\s*rgba\(0,0,0,0\.[0-9]+\);?", "color: var(--text); opacity: 0.6;", css)
css = re.sub(r"color:\s*var\(--muted\);?", "color: var(--text); opacity: 0.6;", css)
css = re.sub(r"color:\s*var\(--text-2\);?", "color: var(--text); opacity: 0.8;", css)

# Fix background of active buttons from the old blue to accent
css = css.replace('background: #007AFF;', 'background: var(--accent);')

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Font and accent colors consolidated!")
