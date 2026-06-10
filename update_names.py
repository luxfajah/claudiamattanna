import re

js_files = ['abril.js', 'maio.js']

for filepath in js_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace juximendes with claudiamattanna_
    content = content.replace('juximendes', 'claudiamattanna_')
    
    # Replace Juliana Ximendes with Gabriela Saueressig
    content = content.replace('Juliana Ximendes', 'Gabriela Saueressig')
    
    # Update currentUser logic in addComment (or similar functions)
    content = re.sub(
        r"currentUser === 'ximenas@duasmaos\.com\.br' \|\| currentUser === 'ximenas' \|\| currentUser === 'juliana@duasmaos\.com\.br' \|\| currentUser === 'juliana'",
        r"currentUser === 'gabriela' || currentUser === 'gabriela@duasmaos.com.br'",
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
