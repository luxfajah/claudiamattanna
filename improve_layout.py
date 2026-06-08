import re

# 1. Update index.html
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

index = index.replace(
    "display: flex; align-items: center; justify-content: center;",
    "display: flex; align-items: flex-end; justify-content: flex-start; padding: 40px 60px;"
)
index = index.replace(
    "text-align: center; padding: 60px 24px; max-width: 700px;",
    "text-align: left; padding: 0 0 60px 0; max-width: 700px;"
)
index = index.replace(
    "margin: 22px auto; opacity: .55;",
    "margin: 22px 0; opacity: .55;"
)
index = index.replace(
    "display: flex; gap: 20px; justify-content: center;",
    "display: flex; gap: 20px; justify-content: flex-start;"
)

# Update logo alignment
index = index.replace(
    "margin: 20px 0 16px;",
    "margin: 20px 0 24px;"
)

with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index)


# 2. Update junho.html
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho = f.read()

junho = junho.replace("ginecogabrielasaueressig", "claudiamattanna")

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(junho)


# 3. Update junho.css spacing
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# info-panel padding
css = re.sub(r"padding:\s*60px\s*48px;", "padding: 80px 60px;", css)
# post-split gap
css = re.sub(r"(\.post-split\s*\{[^}]*)gap:\s*40px;", r"\1gap: 80px;", css)
css = re.sub(r"(\.overview-split\s*\{[^}]*)gap:\s*60px;", r"\1gap: 100px;", css)
# igp-top
css = re.sub(r"padding:\s*40px\s*60px\s*20px;", "padding: 60px 60px 30px;", css)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Layout improvements applied!")
