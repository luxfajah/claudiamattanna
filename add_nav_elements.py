import re

# 1. Update index.html to add photo to portal-box
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

portal_box_pattern = r'<div class="portal-box">\s*<h1>Plataforma de Aprovação</h1>'
new_portal_box = """<div class="portal-box">
    <div class="ig-ava-placeholder" style="width:80px; height:80px; margin-bottom: 24px;">
      <img src="foto.jpg" alt="Claudia Mattanna">
    </div>
    <h1>Plataforma de Aprovação</h1>"""

index_html = re.sub(portal_box_pattern, new_portal_box, index_html)

with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# 2. Update junho.html to add "Sair" button
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho_html = f.read()

# We need to add the exit button inside the dashboard header.
# Let's add it inside .dh-container, maybe absolutely positioned at the top right, or as a small link.
# Or better, add a top-bar above dh-container, or just inside dh-client.
# Let's put it as a discrete "Voltar ao Portal" button at the very top of .dashboard-header.

header_pattern = r'<header class="dashboard-header reveal">\s*<div class="dh-container">'
exit_btn_html = """<header class="dashboard-header reveal" style="flex-direction: column; align-items: center;">
  <div style="width: 100%; max-width: 1200px; display: flex; justify-content: flex-start; margin-bottom: 16px;">
    <a href="index.html" style="display: inline-flex; align-items: center; gap: 8px; color: #fff; text-decoration: none; font-size: 13px; font-weight: 500; opacity: 0.8; transition: opacity 0.2s;">
      <span class="material-symbols-outlined" style="font-size: 18px;">arrow_back</span> Voltar ao Portal
    </a>
  </div>
  <div class="dh-container">"""

junho_html = re.sub(header_pattern, exit_btn_html, junho_html)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(junho_html)

print("Photo and exit button added!")
