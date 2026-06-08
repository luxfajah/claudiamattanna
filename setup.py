import os
import re

# Colors from Palette
AZUL_PROFUNDO = "#2C3E4A"
AZUL_ACO = "#4A6F82"
AZUL_NEVOA = "#B8CDD6"
BRANCO = "#FFFFFF"
DOURADO = "#B8975A"
GRAFITE = "#2C2C2C"

def replace_in_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Update index.html
index_replacements = [
    ('Gabriela Saueressig', 'Claudia Mattanna'),
    ('pexels-didsss-19856128.webp', 'bg.jpg'),
    ('<img src="logos/logo header.webp" alt="Claudia Mattanna">', '<h1 style="color:#fff; font-family:\'Playfair Display\', serif; font-size:32px; margin-bottom:20px; font-weight:normal;">Claudia Mattanna</h1>'),
    ('<img src="logos/logo header.webp" alt="Claudia Mattanna" class="hero-logo"/>', '<h1 class="hero-logo" style="color:#fff; font-family:\'Playfair Display\', serif; font-size:clamp(40px, 8vw, 70px); font-weight:normal; margin: 30px 0;">Claudia Mattanna</h1>'),
    ('--bg:         #F8F6F4;', f'--bg:         {BRANCO};'),
    ('--text:       #1C1817;', f'--text:       {AZUL_PROFUNDO};'),
    ('--gold:       #C4A882;', f'--gold:       {DOURADO};'),
    ('<a href="abril.html" class="btn-month">Entregas de Abril</a>\n      <a href="maio.html" class="btn-month">Entregas de Maio</a>', '<a href="junho.html" class="btn-month">Entregas de Junho</a>'),
    ('background: #2E4F3E;', f'background: {AZUL_PROFUNDO};'),
    ('rgba(6, 95, 70, 0.12)', 'rgba(74, 111, 130, 0.2)')
]
replace_in_file('/Users/luxfajah/claudia_mattanna/index.html', index_replacements)

# 2. Update build_junho.py
build_replacements = [
    ("open('/Users/luxfajah/gabriela/maio.html', 'r', encoding='utf-8')", "open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8')"),
    ("open('/Users/luxfajah/gabriela/maio.html', 'w', encoding='utf-8')", "open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8')"),
    ("Gabriela Saueressig", "Claudia Mattanna"),
    ("gabrielasaueressig_", "claudiamattanna"),
    ("maio.css", "junho.css"),
    ("maio.js", "junho.js"),
    ("Entregas de Maio", "Entregas de Junho"),
    ("Planejamento de conteúdo · Maio 2026", "Planejamento de conteúdo · Junho 2026"),
    ("Planejamento · Maio 2026", "Planejamento · Junho 2026"),
    ("Ginecologia & Cirurgia Ginecológica", "Ginecologia Endócrina"),
    ("🔗 linktr.ee/ginecogabrielasaueressig", "🔗 linktr.ee/claudiamattanna"),
    ("Dor na relação não é normal!<br>Com avaliação adequada, é possível entender a causa e traçar o melhor tratamento pra cada caso.", "Ginecologia com precisão e cuidado humano.<br>Acompanhamento focado no bem-estar endócrino e feminino."),
    ("foto.webp", "foto.jpg"),
    ("Maio/", "Junho/")
]
replace_in_file('/Users/luxfajah/claudia_mattanna/build_junho.py', build_replacements)

# 3. Update junho.css
css_replacements = [
    ('--bg-color: #F8F6F4;', f'--bg-color: {BRANCO};'),
    ('--text-main: #1C1817;', f'--text-main: {GRAFITE};'),
    ('--text-muted: #5C524E;', f'--text-muted: {AZUL_ACO};'),
    ('--accent: #C4A882;', f'--accent: {DOURADO};'),
    ('--accent-hover: #B0946E;', f'--accent-hover: {AZUL_PROFUNDO};'),
    ('--border: rgba(28,24,23,0.08);', '--border: rgba(44,62,74,0.1);'),
    ('--surface: #FFFFFF;', f'--surface: {BRANCO};'),
    ('--badge-bg: #EAE3D9;', f'--badge-bg: {AZUL_NEVOA};'),
    ('--badge-text: #6B553D;', f'--badge-text: {AZUL_PROFUNDO};'),
    ('--header-bg: rgba(248,246,244,0.85);', f'--header-bg: rgba(255,255,255,0.85);'),
    ('--success: #2E4F3E;', '--success: #2C3E4A;'),
    ('font-family: \'Canela\'', 'font-family: \'Playfair Display\''),
    ('.pi-item.active { background: var(--text-main); color: var(--bg-color); }', '.pi-item.active { background: var(--accent); color: var(--bg-color); border-color: var(--accent); }')
]
replace_in_file('/Users/luxfajah/claudia_mattanna/junho.css', css_replacements)

print("Setup complete")
