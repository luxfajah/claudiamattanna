import re

with open('/Users/luxfajah/claudia_mattanna/build_junho.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace numbers
content = content.replace("0 de 8 aprovados", "0 de 3 aprovados")
content = content.replace("8 posts", "3 posts")
content = content.replace("8 posts estratégicos", "3 posts estratégicos")
content = content.replace('id="f-pending">8<', 'id="f-pending">3<')
content = content.replace("range(1, 9)", "range(1, 4)")

# Replace posts_data
new_posts_data = """posts_data = [
    {
        'id': '1', 'title': 'Post 1', 'type': 'Carrossel', 'caption': 'Carrossel 1 — Aprovação pendente',
        'slides': ['Post 1 - 1.png', 'Post 1 - 2.png', 'Post 1 - 3.png', 'Post 1 - 4.png', 'Post 1 - 5.png', 'Post 1 - 6.png'],
        'folder': 'Junho/Post 1'
    },
    {
        'id': '2', 'title': 'Post 2', 'type': 'Carrossel', 'caption': 'Carrossel 2 — Aprovação pendente',
        'slides': ['Post 2 - 1.png', 'Post 2 - 2.png', 'Post 2 - 3.png', 'Post 2 - 4.png'],
        'folder': 'Junho/Post 2'
    },
    {
        'id': '3', 'title': 'Post 3', 'type': 'Imagem', 'caption': 'Imagem Única — Aprovação pendente',
        'media': '<img src="Junho/Post 3/Post 3.png" style="width:100%; height:auto; display:block;" alt="Post 3" loading="lazy">',
        'grid_media': '<img src="Junho/Post 3/Post 3.png" alt="Post 3" loading="lazy" decoding="async">'
    }
]"""

# Regex to replace posts_data completely
content = re.sub(r'posts_data = \[.*?\n\]', new_posts_data, content, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/build_junho.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Posts updated in build script")
