import re

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r') as f:
    js = f.read()

new_lbSources = """  const lbSources = {
    '1': ['Junho/Post 1/Post 1 - 1.png', 'Junho/Post 1/Post 1 - 2.png', 'Junho/Post 1/Post 1 - 3.png', 'Junho/Post 1/Post 1 - 4.png', 'Junho/Post 1/Post 1 - 5.png', 'Junho/Post 1/Post 1 - 6.png'],
    '2': ['Junho/Post 2/Post 2 - 1.png', 'Junho/Post 2/Post 2 - 2.png', 'Junho/Post 2/Post 2 - 3.png', 'Junho/Post 2/Post 2 - 4.png'],
    '3': ['Junho/Post 3/Post 3.png']
  };"""

new_postMeta = """  const postMeta = {
    '1': { caption: 'Carrossel 1 — Aprovação pendente', cards: [] },
    '2': { caption: 'Carrossel 2 — Aprovação pendente', cards: [] },
    '3': { caption: 'Imagem Única — Aprovação pendente', cards: [] }
  };"""

js = re.sub(r'const lbSources = \{.*?\n  \};', new_lbSources, js, flags=re.DOTALL)
js = re.sub(r'const postMeta = \{.*?\n  \};', new_postMeta, js, flags=re.DOTALL)

# Let's also fix the handle inside `populateLbRight` 
js = js.replace("<strong>gabrielasaueressig_</strong>", "<strong>claudiamattanna</strong>")

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w') as f:
    f.write(js)

print("Fixed lbSources in junho.js")
