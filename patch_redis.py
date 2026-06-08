import re
import os

paths = [
    '/Users/luxfajah/claudia_mattanna/api/save.js',
    '/Users/luxfajah/Documents/Duas mâos/Claudia Mattana/api/save.js',
    '/Users/luxfajah/claudia_mattanna/api/load.js',
    '/Users/luxfajah/Documents/Duas mâos/Claudia Mattana/api/load.js'
]

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            js = f.read()
        
        js = js.replace("'gabriela_responses'", "'claudia_responses'")
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(js)

print("Database keys updated!")
