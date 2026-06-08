import re

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix references to Maio
html = html.replace('Maio 2026', 'Junho 2026')

# Post 1
html = html.replace(
    '<span id="eyebrow-1">Carrossel</span>',
    '<span id="eyebrow-1">Carrossel</span> <span class="date">🗓 Quinta, 11 de Junho</span>'
)

# Post 2
html = html.replace(
    '<span id="eyebrow-2">Carrossel</span>',
    '<span id="eyebrow-2">Carrossel</span> <span class="date">🗓 Quinta, 18 de Junho</span>'
)

# Post 3
html = html.replace(
    '<span id="eyebrow-3">Imagem</span>',
    '<span id="eyebrow-3">Imagem</span> <span class="date">🗓 Quinta, 25 de Junho</span>'
)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Also fix the index.html references to Maio if any? Wait, index.html just says "Entregas de Junho"
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()
    
if 'Maio' in index_html:
    index_html = index_html.replace('Maio', 'Junho')
    with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

print("Fixed references to Maio and added June dates!")
