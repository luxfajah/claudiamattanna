with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r') as f:
    js = f.read()

replacements = [
    ("['2','4','6'].forEach(initIG);", "['1','2'].forEach(initIG);"),
    ("const statuses = {1:'none', 2:'none', 3:'none', 4:'none', 5:'none', 6:'none', 7:'none', 8:'none'};", "const statuses = {1:'none', 2:'none', 3:'none'};"),
    ("const total = 8;", "const total = 3;"),
    ("['1','2','3','4','5','6','7','8'].forEach(", "['1','2','3'].forEach("),
    ("'gabriela' || currentUser === 'gabriela@duasmaos.com.br'", "'claudia' || currentUser === 'claudia@duasmaos.com.br'"),
    ("'Gabriela Saueressig'", "'Claudia Mattanna'")
]

for old, new in replacements:
    js = js.replace(old, new)

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w') as f:
    f.write(js)

print("Fixed junho.js")
