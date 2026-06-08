import re
import glob

# Apply Inter font to all CSS and HTML files
for filepath in glob.glob('/Users/luxfajah/claudia_mattanna/*.*'):
    if filepath.endswith('.css') or filepath.endswith('.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Define root variables for Inter if not exist
        if ':root {' in content and '--font-main' not in content:
            content = content.replace(':root {', ":root {\n  --font-main: 'Inter', -apple-system, sans-serif;\n  --font-head: 'Inter', -apple-system, sans-serif;")

        # Redefine any existing font variables
        content = re.sub(r"--font-main:\s*[^;]+;", "--font-main: 'Inter', -apple-system, sans-serif;", content)
        content = re.sub(r"--font-head:\s*[^;]+;", "--font-head: 'Inter', -apple-system, sans-serif;", content)

        # Replace hardcoded Fraunces, Georgia, and other fonts with Inter
        content = re.sub(r"font-family:\s*'Fraunces',\s*serif\s*!*i*m*p*o*r*t*a*n*t*;", "font-family: 'Inter', -apple-system, sans-serif;", content)
        content = re.sub(r"font-family:\s*'Fraunces',\s*serif;", "font-family: 'Inter', -apple-system, sans-serif;", content)
        content = re.sub(r"font-family:\s*Georgia,\s*serif;", "font-family: 'Inter', -apple-system, sans-serif;", content)
        content = re.sub(r"font-family:\s*-apple-system,\s*BlinkMacSystemFont,\s*\"Segoe UI\",\s*Roboto,\s*Helvetica,\s*Arial,\s*sans-serif;", "font-family: 'Inter', -apple-system, sans-serif;", content)

        # Explicitly make sure the HTML files load Inter font from Google Fonts if missing
        if filepath.endswith('.html'):
            if 'fonts.googleapis.com/css2?family=Inter' not in content:
                content = content.replace('</head>', '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n</head>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# Additionally, add a global rule to junho.css to force it, carefully avoiding Material Symbols
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += """
/* ── ENFORCE INTER GLOBALLY ── */
body, h1, h2, h3, h4, h5, h6, p, a, span, div, button, input {
  font-family: 'Inter', -apple-system, sans-serif;
}
.material-symbols-outlined {
  font-family: 'Material Symbols Outlined' !important;
}
"""

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Font universally changed to Inter!")
