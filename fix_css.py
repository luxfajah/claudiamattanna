import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace root variables
new_root = """    :root {
      --bg: #FFFFFF;
      --white:      #FFFFFF;
      --border:     #B8CDD6;
      --border-2:   #4A6F82;
      --text:       #2C3E4A;
      --text-2:     #4A6F82;
      --muted:      #4A6F82;
      --purple: #2C2C2C;
      --purple-mid: #4A6F82;
      --purple-lt: #B8CDD6;
      --rose: #B8975A;
      --rose-lt: #FFFDF5;
      --neutral:    #F5F7F8;
      --neutral-2:  #B8CDD6;
      --gold: #B8975A;
      --beige:      #FFFFFF;
      --note-bg:    #FFFFFF;
      --note-line:  #B8CDD6;
      --radius:     20px;
      --radius-sm:  12px;
      --radius-pill:50px;
      --shadow:     0 2px 16px rgba(44,62,74,.07);
      --shadow-lg:  0 8px 40px rgba(44,62,74,.11);
      --shadow-xl:  0 20px 80px rgba(44,62,74,.15);
    }"""

css = re.sub(r':root\s*\{[^}]*\}', new_root, css, flags=re.DOTALL)

# Fix hero-bg gradient
new_hero_bg = """    .hero-bg {
      position: fixed; inset: 0;
      width: 100%; height: 100%;
      background: url('bg.jpg') center/cover no-repeat;
      z-index: 0;
      pointer-events: none;
      filter: saturate(1.1) brightness(0.85);
      will-change: transform;
      transform: scale(1.05);
    }"""

css = re.sub(r'\.hero-bg\s*\{[^}]*\}', new_hero_bg, css, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed junho.css variables and hero background!")
