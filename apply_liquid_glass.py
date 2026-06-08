import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

liquid_shadow = "box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.5), 0 8px 32px rgba(0, 0, 0, 0.08);"

# Apply to info-panel
css = re.sub(
    r"(\.info-panel\s*\{[^}]*)box-shadow:\s*0 8px 32px rgba\([^)]+\);",
    r"\1" + liquid_shadow,
    css
)

# Replace existing box-shadows on igp
css = re.sub(
    r"(\.igp\s*\{[^}]*)box-shadow:\s*var\(--shadow-lg\);",
    r"\1" + liquid_shadow,
    css
)

# Replace on post-panel
css = re.sub(
    r"(\.post-panel\s*\{[^}]*)box-shadow:\s*var\(--shadow-md\);",
    r"\1" + liquid_shadow,
    css
)

# tactile feedback
tactile_css = """
.btn-pri:active, .btn-sec:active, .abtn:active, .modal-btn:active, .download-post-btn:active, .dl-card:active {
  transform: scale(0.98) !important;
  transition: transform 0.05s ease !important;
}
"""

css += "\n" + tactile_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html for index login-box tactile feedback
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

index = index.replace(
    ".btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(122, 30, 80, 0.3); }",
    ".btn-primary:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0, 122, 255, 0.3); }\n    .btn-primary:active { transform: scale(0.98) !important; transition: transform 0.05s ease !important; }"
)

with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

print("Liquid glass applied!")
