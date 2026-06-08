import re

def inject_font(html):
    link = '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />'
    if 'Material+Symbols+Outlined' not in html:
        return html.replace('<link href="https://fonts.googleapis.com/css2?family=Playfair', link + '\n  <link href="https://fonts.googleapis.com/css2?family=Playfair')
    return html

# 1. Update index.html
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

index = inject_font(index)
# Replace any known emojis or arrows if any (no obvious ones in index, but just in case)
with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

# 2. Update junho.html
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho = f.read()

junho = inject_font(junho)

# Replace symbols
junho = junho.replace('>‹<', '><span class="material-symbols-outlined">chevron_left</span><')
junho = junho.replace('>›<', '><span class="material-symbols-outlined">chevron_right</span><')
junho = junho.replace('↺ Limpar', '<span class="material-symbols-outlined" style="font-size:16px; vertical-align:text-bottom;">refresh</span> Limpar')
junho = junho.replace('>✕<', '><span class="material-symbols-outlined">close</span><')

# Toast HTML structure
# toast currently has: <span class="ti"></span><span class="tm"></span>
junho = junho.replace('class="ti"', 'class="ti material-symbols-outlined"')

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(junho)

# 3. Update junho.js
with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace emojis in js
js = js.replace("'✅'", "'check_circle'")
js = js.replace("'✏️'", "'edit'")
js = js.replace("'⏳'", "'schedule'")
js = js.replace("'💬'", "'chat'")
js = js.replace("'🔄'", "'sync'")
js = js.replace("'❌'", "'error'")
js = js.replace("'☁️'", "'cloud_done'")
# "Ver comentários" might have emoji?
js = js.replace('💬 Ver comentários', '<span class=\"material-symbols-outlined\" style=\"font-size:14px; vertical-align:text-bottom;\">chat</span> Ver comentários')

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 4. Update junho.css for Material Symbols font alignment
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r"#toast \.ti\s*\{[^}]*\}",
    "#toast .ti { font-size:20px; font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24; }",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Google Material Symbols integrated!")
