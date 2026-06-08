import re

# Update HTML
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Junho/Post 1/Post 1', 'Junho/Post 1')
html = html.replace('Junho/Post 2/Post 2', 'Junho/Post 2')

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update JS
with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('Junho/Post 1/Post 1', 'Junho/Post 1')
js = js.replace('Junho/Post 2/Post 2', 'Junho/Post 2')

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Paths fixed to remove subfolders!")
