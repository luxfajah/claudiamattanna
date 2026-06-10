def replace_all(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = [
        ('Gabriela Saueressig', 'Claudia Mattanna'),
        ('claudiamattanna_', 'claudiamattanna'),
        ('foto.webp', 'foto.jpg'),
        ('Juliana Ximendes', 'Claudia Mattanna'),
        ('juximendes', 'claudiamattanna'),
        ('0 de 8 aprovados', '0 de 3 aprovados'),
        ('8 posts', '3 posts'),
        ('8 posts estratégicos', '3 posts estratégicos')
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_all('/Users/luxfajah/claudia_mattanna/junho.html')
print("Fixed junho.html")
