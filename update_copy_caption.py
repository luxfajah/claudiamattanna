import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add new CSS classes
new_css = """
/* ── Copy vs Legenda ── */
.content-groups {
  display: flex; flex-direction: column; gap: 24px; padding-top: 8px;
}
.content-group {
  display: flex; flex-direction: column; gap: 12px;
}
.cg-header {
  display: flex; align-items: center; gap: 6px;
  font-size: 11px; font-weight: 700; color: rgba(0,0,0,0.4);
  text-transform: uppercase; letter-spacing: 0.05em;
}
.cg-header .material-symbols-outlined { font-size: 16px; color: rgba(0,0,0,0.5); }

.copy-cards {
  display: flex; flex-direction: column; gap: 8px;
}
.copy-card {
  background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.06);
  padding: 14px 16px; border-radius: 14px;
  font-size: 13.5px; line-height: 1.5; color: var(--text);
}
.copy-card strong { color: #000; font-weight: 700; display: block; margin-bottom: 4px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.03em; }

.caption-body {
  background: #fff; border: 1px solid rgba(0,0,0,0.08);
  padding: 16px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);
  font-size: 13.5px; line-height: 1.5; color: var(--text);
}
.caption-body .handle { font-weight: 700; color: #000; display: inline-block; margin-bottom: 8px; }
"""

if ".content-groups {" not in css:
    css += new_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update junho.html
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace block for post 1
p1_old = r'<div class="caption-blk">\s*<span class="handle">claudiamattanna</span> <strong>\[Carrossel\] Apresentação</strong>.*?CRM n\. XXXX\s*</div>'
p1_new = """<div class="caption-blk" style="padding: 0; background: transparent; border-radius: 0;">
  <div class="content-groups">
    <!-- Grupo Copy -->
    <div class="content-group">
      <div class="cg-header">
        <span class="material-symbols-outlined">view_carousel</span> Texto das Artes (Copy)
      </div>
      <div class="copy-cards">
        <div class="copy-card"><strong>Lâmina 01</strong> Antes de ser médica, fui engenheira, você sabia? Como a vida não é linear, em determinado momento, me fiz uma pergunta que mudou minha história: que outra faculdade vai me dar uma resposta diferente da vida?<br>Foi assim que cheguei na Medicina. No quinto período, já sabia qual seria a minha especialidade: Ginecologia e Obstetrícia. Isso porque já me encantava o fato de a mulher querer entender, querer participar e realmente se importar com a própria saúde.</div>
        <div class="copy-card"><strong>Lâmina 02</strong> Eu também sou paciente e há algumas coisas que me incomodam fortemente:<br>- quando não há clareza na explicação e a consulta é muito mais protocolar do que cuidado efetivo;<br>- quando a conduta é protocolo e não há foco na pessoa.<br>Então, venho construindo uma prática que vai ao oposto disso.</div>
        <div class="copy-card"><strong>Lâmina 03</strong> O que você vai encontrar comigo?<br>Uma consulta com começo, meio e fim, com raciocínio clínico que considera o seu histórico, a sua rotina e a sua fase de vida, além de ensino prático, para que você realmente entenda tudo o que foi combinado e quais as implicações de cada ação na sua vida.</div>
        <div class="copy-card"><strong>Lâmina 04</strong> A educação é parte fundamental do meu cuidado, pois quando a mulher entende realmente o que acontece com o seu corpo, passa a tomar melhores decisões.</div>
        <div class="copy-card"><strong>Lâmina 05</strong> Me chamo Cláudia Mattana. Sou ginecologista. E amo estar com mulheres que querem aprender, buscam se cuidar e alcançarem uma melhor qualidade de vida.<br>Se quiser conhecer melhor o meu trabalho, fica por aqui. Será um prazer te conhecer mais e caminhar contigo.</div>
      </div>
    </div>
    <!-- Grupo Legenda -->
    <div class="content-group">
      <div class="cg-header">
        <span class="material-symbols-outlined">notes</span> Legenda do Post
      </div>
      <div class="caption-body">
        <span class="handle">claudiamattanna</span>
        Um abraço,<br>Cláudia Mattana<br>RQE n. XXXX<br>CRM n. XXXX
      </div>
    </div>
  </div>
</div>"""

# Replace block for post 2
p2_old = r'<div class="caption-blk">\s*<span class="handle">claudiamattanna</span> <strong>\[Carrossel\] Posicionamento</strong>.*?volta a viver com mais segurança\.\s*</div>'
p2_new = """<div class="caption-blk" style="padding: 0; background: transparent; border-radius: 0;">
  <div class="content-groups">
    <!-- Grupo Copy -->
    <div class="content-group">
      <div class="cg-header">
        <span class="material-symbols-outlined">view_carousel</span> Texto das Artes (Copy)
      </div>
      <div class="copy-cards">
        <div class="copy-card" style="color:var(--muted); font-style:italic;">(As lâminas deste post contêm apenas títulos curtos visuais)</div>
      </div>
    </div>
    <!-- Grupo Legenda -->
    <div class="content-group">
      <div class="cg-header">
        <span class="material-symbols-outlined">notes</span> Legenda do Post
      </div>
      <div class="caption-body">
        <span class="handle">claudiamattanna</span>
        Você já saiu de uma consulta ginecológica com mais dúvidas do que entrou?<br>Receita na mão, exame pedido, dez minutos de atendimento…<br>E aquela sensação de que você foi vista, mas não foi realmente compreendida de acordo com o seu contexto, ou seja, que o seu corpo foi avaliado, mas a sua vida não foi considerada?<br>Isso não é cuidado, combina mais com triagem, e existe diferença.<br>A mulher que entende o que está acontecendo com o próprio corpo cuida melhor de si, adere ao tratamento e volta a viver com mais segurança.
      </div>
    </div>
  </div>
</div>"""

# Replace block for post 3
p3_old = r'<div class="caption-blk">\s*<span class="handle">claudiamattanna</span> <strong>\[Imagem Única\] Locais de atendimento</strong>.*?apenas a base\)\s*</div>'
p3_new = """<div class="caption-blk" style="padding: 0; background: transparent; border-radius: 0;">
  <div class="content-groups">
    <!-- Grupo Copy -->
    <div class="content-group">
      <div class="cg-header">
        <span class="material-symbols-outlined">image</span> Texto da Imagem (Copy)
      </div>
      <div class="copy-cards">
        <div class="copy-card">Conheça meus locais de atendimento</div>
      </div>
    </div>
    <!-- Grupo Legenda -->
    <div class="content-group">
      <div class="cg-header">
        <span class="material-symbols-outlined">notes</span> Legenda do Post
      </div>
      <div class="caption-body">
        <span class="handle">claudiamattanna</span>
        Inserir endereço (ainda não temos, ela vai confirmar, mas, para amanhã, pode deixar apenas a base)
      </div>
    </div>
  </div>
</div>"""

# Also remove the standalone `<div class="blk-label">Legenda</div>` since it's redundant now
html = re.sub(r'<div class="blk-label">Legenda</div>', '', html)

html = re.sub(p1_old, p1_new, html, flags=re.DOTALL)
html = re.sub(p2_old, p2_new, html, flags=re.DOTALL)
html = re.sub(p3_old, p3_new, html, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Copy and caption split successfully!")
