import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add an absolute override for the indicator and section padding
override_css = """
/* ── FIX INDICATOR OVERLAP ── */
.post-indicator {
  top: 40px !important;
}
.post-section {
  padding-top: 120px !important; /* Pushes the white boxes down safely */
  height: 100% !important;
  box-sizing: border-box !important;
}
"""

css += override_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Indicator spacing fixed!")
