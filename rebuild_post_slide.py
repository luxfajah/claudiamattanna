import re

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = "<!-- ══ POST 1 ══ -->"
end_marker = "<!-- Modal de Erro Persistente -->"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

def build_post(idx, date, type_, title, images, caption):
    arrows = ""
    if len(images) > 1:
        arrows = f'''
          <div class="ig-dots" id="idots-{idx}"></div>
          <button class="ig-arrow prev" onclick="igSlide('{idx}', -1)"><span class="material-symbols-outlined">chevron_left</span></button>
          <button class="ig-arrow next" onclick="igSlide('{idx}', 1)"><span class="material-symbols-outlined">chevron_right</span></button>
'''
    
    img_html = ""
    if len(images) > 1:
        img_html = f'''
        <div class="ig-carousel" style="cursor:pointer" onclick="openLightbox('{idx}')">
          <div class="ig-track" id="itrack-{idx}">
            {''.join([f'<div class="ig-slide"><img src="{img}" loading="lazy" decoding="async"></div>' for img in images])}
          </div>
          {arrows}
        </div>
        '''
    else:
        img_html = f'''
        <div class="ig-carousel" style="cursor:pointer" onclick="openLightbox('{idx}')">
          <img src="{images[0]}" style="width:100%; height:auto; display:block;" alt="Post {idx}" loading="lazy">
        </div>
        '''

    return f'''
<!-- ══ POST {idx} ══ -->
<section class="post-section" id="sec-{idx}" style="position:relative;">
  <div class="post-split">
    
    <!-- LEFT: Image Gallery -->
    <div class="gallery-col reveal">
      {img_html}
    </div>
    
    <!-- RIGHT: Info & Actions -->
    <div class="post-panel reveal" style="transition-delay:.1s">
      <div class="post-head">
        <div class="post-eyebrow">
          <span id="eyebrow-{idx}">{type_}</span> <span class="date">🗓 {date}</span>
          <span class="v3-badge">v1</span>
        </div>
        <h3 class="post-title">Peça 0{idx} — <em>{title}</em></h3>
        <div class="sb sb-none" id="badge-{idx}"><span class="sbp"></span>Aguardando</div>
      </div>
      <div class="blk-label">Legenda</div>
      <div class="caption-blk">
        <span class="handle">claudiamattanna</span> <strong>[{type_}] {title}</strong><br><br>
        {caption}
      </div>
      
      <div class="panel-actions-wrapper">
        <div class="reject-alert" id="ralert-{idx}">⚠ Para reprovar, adicione um comentário primeiro.</div>
        <div class="actions">
          <div class="actions-left">
            <button class="abtn btn-ap" id="ba-{idx}" onclick="event.stopPropagation(); setStatus('{idx}','approved')"><span class="material-symbols-outlined" style="font-size:18px;">check</span> Aprovar</button>
            <button class="abtn btn-rj" id="br-{idx}" onclick="event.stopPropagation(); setStatus('{idx}','rejected')"><span class="material-symbols-outlined" style="font-size:18px;">close</span> Reprovar</button>
            <button class="abtn btn-lt" id="bl-{idx}" onclick="event.stopPropagation(); openReviewModal('{idx}')"><span class="material-symbols-outlined" style="font-size:18px;">schedule</span> Revisar</button>
          </div>
          <button class="abtn btn-cm" id="bc-{idx}" onclick="event.stopPropagation(); openCommentsModal('{idx}')"><span class="material-symbols-outlined" style="font-size:18px;">chat</span> Comentários</button>
        </div>
      </div>
    </div>
    
  </div>
</section>
'''

post1 = build_post(
    "1", "Quinta, 11 de Junho", "Carrossel", "Apresentação", 
    [f"Junho/Post 1 - {i}.png" for i in range(1, 7)],
    "<strong>Card 1:</strong> Antes de ser médica, fui engenheira, você sabia? Como a vida não é linear, em determinado momento, me fiz uma pergunta que mudou minha história: que outra faculdade vai me dar uma resposta diferente da vida?<br>Foi assim que cheguei na Medicina. No quinto período, já sabia qual seria a minha especialidade: Ginecologia e Obstetrícia. Isso porque já me encantava o fato de a mulher querer entender, querer participar e realmente se importar com a própria saúde.<br><br><strong>Card 2:</strong> Eu também sou paciente e há algumas coisas que me incomodam fortemente:<br>- quando não há clareza na explicação e a consulta é muito mais protocolar do que cuidado efetivo;<br>- quando a conduta é protocolo e não há foco na pessoa.<br>Então, venho construindo uma prática que vai ao oposto disso.<br><br><strong>Card 3:</strong> O que você vai encontrar comigo?<br>Uma consulta com começo, meio e fim, com raciocínio clínico que considera o seu histórico, a sua rotina e a sua fase de vida, além de ensino prático, para que você realmente entenda tudo o que foi combinado e quais as implicações de cada ação na sua vida.<br><br><strong>Card 4:</strong> A educação é parte fundamental do meu cuidado, pois quando a mulher entende realmente o que acontece com o seu corpo, passa a tomar melhores decisões.<br><br><strong>Card 5:</strong> Me chamo Cláudia Mattana. Sou ginecologista. E amo estar com mulheres que querem aprender, buscam se cuidar e alcançarem uma melhor qualidade de vida.<br>Se quiser conhecer melhor o meu trabalho, fica por aqui. Será um prazer te conhecer mais e caminhar contigo.<br><br>Um abraço,<br>Cláudia Mattana<br>RQE n. XXXX<br>CRM n. XXXX"
)

post2 = build_post(
    "2", "Quinta, 18 de Junho", "Carrossel", "Posicionamento",
    [f"Junho/Post 2 - {i}.png" for i in range(1, 5)],
    "Você já saiu de uma consulta ginecológica com mais dúvidas do que entrou?<br>Receita na mão, exame pedido, dez minutos de atendimento…<br>E aquela sensação de que você foi vista, mas não foi realmente compreendida de acordo com o seu contexto, ou seja, que o seu corpo foi avaliado, mas a sua vida não foi considerada?<br>Isso não é cuidado, combina mais com triagem, e existe diferença.<br>A mulher que entende o que está acontecendo com o próprio corpo cuida melhor de si, adere ao tratamento e volta a viver com mais segurança."
)

post3 = build_post(
    "3", "Quinta, 25 de Junho", "Imagem Única", "Locais de atendimento",
    ["Junho/Post 3.png"],
    "Conheça meus locais de atendimento<br><br>Inserir endereço (ainda não temos, ela vai confirmar, mas, para amanhã, pode deixar apenas a base)"
)

new_content = start_marker + "\n" + post1 + post2 + post3 + "\n</div>\n</section>\n\n\n"

new_html = html[:start_idx] + new_content + html[end_idx:]

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# CSS Update
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r"\.post-split\s*\{[^}]*\}",
    """
.post-split {
  display: grid; grid-template-columns: minmax(320px, 1fr) minmax(320px, 1.2fr); gap: 40px;
  width: 100%; max-width: 1300px;
  margin: 0 auto; align-items: start;
}
""",
    css
)

css += """
.gallery-col {
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  background: transparent; border-radius: 24px; overflow: hidden; position: relative;
  width: 100%;
}
.gallery-col .ig-carousel {
  width: 100%; height: auto; position: relative; border-radius: 24px; overflow: hidden;
  box-shadow: 0 16px 40px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.4);
}
.gallery-col .ig-track {
  display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none;
}
.gallery-col .ig-track::-webkit-scrollbar { display: none; }
.gallery-col .ig-slide {
  min-width: 100%; display: flex; align-items: center; justify-content: center;
}
.gallery-col .ig-slide img {
  width: 100%; height: auto; object-fit: contain; display: block;
}
.panel-actions-wrapper {
  margin-top: 32px; padding-top: 24px; border-top: 1px solid rgba(0,0,0,0.06);
}
.panel-actions-wrapper .actions {
  display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap;
}
.panel-actions-wrapper .actions-left {
  display: flex; gap: 12px; flex: 1; flex-wrap: wrap;
}
.abtn { display: inline-flex; align-items: center; gap: 6px; }
"""

# Remove old broken scale transition logic
css = re.sub(r"\.post-split\s*\{\s*transform:\s*scale[^}]*\}", "", css)
css = re.sub(r"\.post-section\.active-slide\s*\.post-split\s*\{[^}]*\}", "", css)
css = re.sub(r"\.post-actions-below\s*\{[^}]*\}", ".post-actions-below { display: none; }", css)

# Fix mobile
css = re.sub(
    r"@media\(max-width:\s*900px\)\s*\{",
    """@media(max-width: 900px) {
  .post-split { grid-template-columns: 1fr; gap: 24px; }
  .panel-actions-wrapper .actions { flex-direction: column; }
  .panel-actions-wrapper .actions-left { flex-direction: column; }
  .abtn { justify-content: center; width: 100%; }
  .posts-horizontal-track { padding: 0 5vw; gap: 10vw; }
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Slide rebuilt completely!")
