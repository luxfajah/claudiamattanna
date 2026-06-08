import re
import os

links = [
    'https://drive.google.com/drive/folders/1c7cqJtzfB2OU_U0svTbUSfCU9dt0Us1L?usp=drive_link',
    'https://drive.google.com/drive/folders/1tND2j22beJ2xSMnHA10IgY44IACy32Ck?usp=drive_link',
    'https://drive.google.com/drive/folders/1LcYiRRTyNih4IN4YXzrD9lIn-FZG9yb2?usp=drive_link',
    'https://drive.google.com/drive/folders/1CE8sJmRfx2WpQLW3tq5SnOicM4hJFXN2?usp=drive_link'
]

paths = [
    '/Users/luxfajah/claudia_mattanna/junho.html',
    '/Users/luxfajah/Documents/Duas mâos/Claudia Mattana/junho.html'
]

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update Pasta Completa
        html = re.sub(
            r'<a href="[^"]*" class="abtn btn-pri"([^>]*)>',
            f'<a href="{links[0]}" class="abtn btn-pri" target="_blank"\\1>',
            html
        )

        # Update Post 1
        html = re.sub(
            r'<a href="[^"]*"\s+class="dl-item"([^>]*)>(\s*<div class="dl-icon">01</div>)',
            f'<a href="{links[1]}" class="dl-item" target="_blank"\\1>\\2',
            html
        )

        # Update Post 2
        html = re.sub(
            r'<a href="[^"]*"\s+class="dl-item"([^>]*)>(\s*<div class="dl-icon">02</div>)',
            f'<a href="{links[2]}" class="dl-item" target="_blank"\\1>\\2',
            html
        )

        # Update Post 3
        html = re.sub(
            r'<a href="[^"]*"\s+class="dl-item"([^>]*)>(\s*<div class="dl-icon">03</div>)',
            f'<a href="{links[3]}" class="dl-item" target="_blank"\\1>\\2',
            html
        )

        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print("Links updated successfully!")
