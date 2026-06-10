import re

# Read clean base HTML
with open('/Users/luxfajah/gabriela/maio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the bug with the non-greedy regex!
# Instead of regex, let's slice it perfectly.
start_marker = '<div class="posts-horizontal-track" id="mainPostsTrack">'
end_marker = '<div id="hiddenCommentsData" style="display:none">'

part1 = html.split(start_marker)[0]
part2 = html.split(end_marker)[1]

# Now we apply all our custom posts data
posts_data = [
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
]

main_posts_html = ""
for p in posts_data:
    if 'slides' in p:
        slides_html = ""
        for s in p['slides']:
            slides_html += f'<div class="ig-slide"><img src="{p["folder"]}/{s}" loading="lazy" decoding="async"></div>\n            '
        media_html = f"""<div class="ig-carousel" style="cursor:pointer" onclick="openLightbox('{p['id']}')">
          <div class="ig-track" id="itrack-{p['id']}">
            {slides_html}
          </div>
          <div class="ig-dots" id="idots-{p['id']}"></div>
          <button class="ig-arrow prev" onclick="igSlide('{p['id']}', -1)">‹</button>
          <button class="ig-arrow next" onclick="igSlide('{p['id']}', 1)">›</button>
        </div>"""
    else:
        media_html = f"""<div class="ig-carousel" style="cursor:pointer" onclick="openLightbox('{p['id']}')">
          {p['media']}
        </div>"""

    main_posts_html += f"""
<!-- ══ POST {p['id']} ══ -->
<section class="post-section" id="sec-{p['id']}" style="position:relative;">
  <div class="post-split">
    <div class="reveal">
      <div class="post-num-badge"><div class="pnb-dot">{p['id']}</div> Post {p['id']}</div>
      <div class="ig-phone">
        <div class="ig-bar">
          <div class="ig-ava"><img src="foto.jpg" alt="Claudia Mattanna"></div>
          <div><div class="ig-handle">claudiamattanna</div></div>
          <div class="ig-type" id="type-{p['id']}">{p['type']}</div>
        </div>
        {media_html}
        <div class="ig-foot">
          <p class="ig-cap"><strong>claudiamattanna</strong> Planejamento de conteúdo em aprovação.</p>
        </div>
      </div>
    </div>
    <div class="post-panel reveal" style="transition-delay:.1s">
      <div class="post-head">
        <div class="post-eyebrow">
          <span id="eyebrow-{p['id']}">{p['type']}</span>
          <span class="v3-badge">v1</span>
        </div>
        <h3 class="post-title">Peça 0{p['id']} — <em>{p['title']}</em></h3>
        <div class="sb sb-none" id="badge-{p['id']}"><span class="sbp"></span>Aguardando</div>
      </div>
      <div class="blk-label">Legenda</div>
      <div class="caption-blk">
        <span class="handle">claudiamattanna</span> {p['caption']}
      </div>
    </div>
  </div>
  <div class="post-actions-below">
    <div class="reject-alert" id="ralert-{p['id']}">⚠ Para reprovar, adicione um comentário primeiro.</div>
    <div class="actions">
      <div class="actions-left">
        <button class="abtn btn-ap" id="ba-{p['id']}" onclick="event.stopPropagation(); setStatus('{p['id']}','approved')">✓ Aprovar</button>
        <button class="abtn btn-rj" id="br-{p['id']}" onclick="event.stopPropagation(); setStatus('{p['id']}','rejected')">✎ Reprovar</button>
        <button class="abtn btn-lt" id="bl-{p['id']}" onclick="event.stopPropagation(); openReviewModal('{p['id']}')">⏳ Revisar</button>
      </div>
      <button class="abtn btn-cm" id="bc-{p['id']}" onclick="event.stopPropagation(); openCommentsModal('{p['id']}')">💬 Comentários</button>
    </div>
  </div>
</section>
"""

mid_content = f'{start_marker}\n{main_posts_html}\n</div>\n</section>\n\n<div id="hiddenCommentsData" style="display:none">\n'
for i in range(1, 4):
    mid_content += f'<div id="comments-{i}"></div>\n'

new_html = part1 + mid_content + part2

# Apply text replacements to the whole HTML
replacements = [
    ('Gabriela Saueressig', 'Claudia Mattanna'),
    ('Juliana Ximendes', 'Claudia Mattanna'),
    ('claudiamattanna_', 'claudiamattanna'),
    ('juximendes', 'claudiamattanna'),
    ('style.css?v=2.2', 'junho.css?v=2.2'),
    ('logos/Foto de perfil.jpg', 'foto.jpg'),
    ('foto.webp', 'foto.jpg'),
    ('0 de 6 aprovados', '0 de 3 aprovados'),
    ('6 posts', '3 posts'),
    ('0 de 8 aprovados', '0 de 3 aprovados'),
    ('8 posts', '3 posts'),
    ('Planejamento de conteúdo · 2026', 'Planejamento de conteúdo · Junho 2026'),
    ('Planejamento · 2026', 'Planejamento · Junho 2026'),
    ('6 posts estratégicos', '3 posts estratégicos'),
    ('8 posts estratégicos', '3 posts estratégicos'),
    ('id="f-pending">6<', 'id="f-pending">3<'),
    ('id="f-pending">8<', 'id="f-pending">3<'),
    ('Juliana Ximendes | Consultoria em Carreira', 'Claudia Mattanna | Ginecologia Endócrina'),
    ('Carreira é escolha consciente. Eu te mostro porquê.<br>\n              Vendas é postura. Eu te mostro o porquê.', 'Ginecologia com precisão e cuidado humano.<br>Acompanhamento focado no bem-estar endócrino e feminino.'),
    ('🔗 linktr.ee/juximendes e mais 1', '🔗 linktr.ee/claudiamattanna'),
    ('Seguido(a) por <strong>dduasmaos</strong>', ''),
    ('dduasmaos.webp', 'duasmaos.webp')
]

for old, new in replacements:
    new_html = new_html.replace(old, new)

# Fix igp-grid (the 3xN grid on the left profile replica)
igp_grid_html = ""
for p in posts_data:
    if 'slides' in p:
        img_src = f"{p['folder']}/{p['slides'][0]}"
        grid_media = f'<img src="{img_src}" alt="{p["title"]}" loading="lazy" decoding="async">'
    else:
        grid_media = p['grid_media']
    igp_grid_html += f"""<div class="igp-grid-item" onclick="openLightbox('{p['id']}')">
      {grid_media}
      <span class="grid-num">0{p['id']}</span>
    </div>"""

new_html = re.sub(r'<div class="igp-grid">.*?</div>\s*</div>\s*</div>\s*</section>', 
              f'<div class="igp-grid">\n{igp_grid_html}\n      </div>\n    </div>\n  </div>\n</section>', new_html, flags=re.DOTALL)

# Fix Indicator
indicator_html = ""
for idx, p in enumerate(posts_data):
    cls = "pi-item active" if idx == 0 else "pi-item"
    indicator_html += f'<div class="{cls}" data-idx="{idx}" onclick="goToPost({idx})">{p["id"]}</div>'
    if idx < len(posts_data) - 1:
        indicator_html += '\n    <div class="pi-sep">–</div>\n    '
new_html = re.sub(r'<div class="post-indicator" id="postIndicator">.*?</div>', f'<div class="post-indicator" id="postIndicator">\n    {indicator_html}\n  </div>', new_html, flags=re.DOTALL)

# Fix Downloads
downloads_grid_html = """
      <a href="#" class="dl-card dl-all">
        <div class="dl-icon">📁</div>
        <div class="dl-info">
          <div class="dl-label">Todos os conteúdos</div>
          <div class="dl-sub">Pasta completa</div>
        </div>
        <div class="dl-arrow">↗</div>
      </a>
"""
for p in posts_data:
    downloads_grid_html += f"""
      <a href="#" class="dl-card">
        <div class="dl-num">0{p['id']}</div>
        <div class="dl-info">
          <div class="dl-label">Post {p['id']}</div>
          <div class="dl-sub">Baixar Arquivo</div>
        </div>
        <div class="dl-arrow">↗</div>
      </a>"""

new_html = re.sub(r'<div class="downloads-grid">.*?</div>\s*</div>\s*</section>', f'<div class="downloads-grid">{downloads_grid_html}\n    </div>\n  </div>\n</section>', new_html, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Rebuilt junho.html perfectly!")
