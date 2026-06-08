import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .post-eyebrow contrast by using the brand text color instead of 40% black
css = re.sub(
    r"\.post-eyebrow\s*\{[^}]*\}",
    """
.post-eyebrow {
  display: flex; align-items: center; gap: 8px; font-size: 11px; 
  color: var(--text); opacity: 0.85; 
  text-transform: uppercase; font-weight: 800; letter-spacing: 0.08em;
}
""",
    css
)

# Also fix the general badge contrast (.sb-none)
css = re.sub(
    r"\.sb-none\s*\{\s*background:\s*#F3F4F6;\s*color:\s*#6B7280;\s*border:\s*1px solid #E5E7EB;\s*\}",
    ".sb-none { background: rgba(44, 62, 74, 0.05); color: var(--text); border: 1px solid rgba(44, 62, 74, 0.15); }",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Contrast fixed!")
