import re

# Read original gabriela/maio.html
with open('/Users/luxfajah/gabriela/maio.html', 'r', encoding='utf-8') as f:
    gabriela_html = f.read()

# Extract from LIGHTBOX to before HIDDEN DATA PERSISTENCE
pattern = r'(<!-- ════════════════════════ LIGHTBOX ════════════════════════ -->.*?)<!-- HIDDEN DATA PERSISTENCE -->'
match = re.search(pattern, gabriela_html, re.DOTALL)
if match:
    modals_html = match.group(1)
else:
    print("Could not find modals in gabriela/maio.html")
    exit(1)

# Read junho.html
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho_html = f.read()

if '<!-- ════════════════════════ LIGHTBOX ════════════════════════ -->' not in junho_html:
    # Insert before <div id="hiddenCommentsData" style="display:none">
    junho_html = junho_html.replace(
        '<div id="hiddenCommentsData" style="display:none">',
        modals_html + '\n<div id="hiddenCommentsData" style="display:none">'
    )
    with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
        f.write(junho_html)
    print("Modals restored!")
else:
    print("Modals already exist.")
