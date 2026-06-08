import re

# Update HTML captions
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

caption_1 = """<span class="handle">claudiamattanna</span> <strong>[Carrossel] Apresentação</strong><br><br>
<strong>Card 1:</strong> Antes de ser médica, fui engenheira, você sabia? Como a vida não é linear, em determinado momento, me fiz uma pergunta que mudou minha história: que outra faculdade vai me dar uma resposta diferente da vida?<br>Foi assim que cheguei na Medicina. No quinto período, já sabia qual seria a minha especialidade: Ginecologia e Obstetrícia. Isso porque já me encantava o fato de a mulher querer entender, querer participar e realmente se importar com a própria saúde.<br><br>
<strong>Card 2:</strong> Eu também sou paciente e há algumas coisas que me incomodam fortemente:<br>- quando não há clareza na explicação e a consulta é muito mais protocolar do que cuidado efetivo;<br>- quando a conduta é protocolo e não há foco na pessoa.<br>Então, venho construindo uma prática que vai ao oposto disso.<br><br>
<strong>Card 3:</strong> O que você vai encontrar comigo?<br>Uma consulta com começo, meio e fim, com raciocínio clínico que considera o seu histórico, a sua rotina e a sua fase de vida, além de ensino prático, para que você realmente entenda tudo o que foi combinado e quais as implicações de cada ação na sua vida.<br><br>
<strong>Card 4:</strong> A educação é parte fundamental do meu cuidado, pois quando a mulher entende realmente o que acontece com o seu corpo, passa a tomar melhores decisões.<br><br>
<strong>Card 5:</strong> Me chamo Cláudia Mattana. Sou ginecologista. E amo estar com mulheres que querem aprender, buscam se cuidar e alcançarem uma melhor qualidade de vida.<br>Se quiser conhecer melhor o meu trabalho, fica por aqui. Será um prazer te conhecer mais e caminhar contigo.<br><br>Um abraço,<br>Cláudia Mattana<br>RQE n. XXXX<br>CRM n. XXXX"""

caption_2 = """<span class="handle">claudiamattanna</span> <strong>[Carrossel] Posicionamento</strong><br><br>
Você já saiu de uma consulta ginecológica com mais dúvidas do que entrou?<br>Receita na mão, exame pedido, dez minutos de atendimento…<br>E aquela sensação de que você foi vista, mas não foi realmente compreendida de acordo com o seu contexto, ou seja, que o seu corpo foi avaliado, mas a sua vida não foi considerada?<br>Isso não é cuidado, combina mais com triagem, e existe diferença.<br>A mulher que entende o que está acontecendo com o próprio corpo cuida melhor de si, adere ao tratamento e volta a viver com mais segurança."""

caption_3 = """<span class="handle">claudiamattanna</span> <strong>[Imagem Única] Locais de atendimento</strong><br><br>
Conheça meus locais de atendimento<br><br>
Inserir endereço (ainda não temos, ela vai confirmar, mas, para amanhã, pode deixar apenas a base)"""

html = re.sub(r'(<h3 class="post-title">Peça 01 — <em>)[^<]*(</em></h3>)', r'\g<1>Apresentação\g<2>', html)
html = re.sub(r'(<h3 class="post-title">Peça 02 — <em>)[^<]*(</em></h3>)', r'\g<1>Posicionamento\g<2>', html)
html = re.sub(r'(<h3 class="post-title">Peça 03 — <em>)[^<]*(</em></h3>)', r'\g<1>Locais de atendimento\g<2>', html)

html = re.sub(r'(<section class="post-section" id="sec-1".*?<div class="caption-blk">\s*).*?(</div>\s*</div>\s*</div>\s*<div class="post-actions-below">)', lambda m: m.group(1) + caption_1 + '\n      ' + m.group(2), html, flags=re.DOTALL)
html = re.sub(r'(<section class="post-section" id="sec-2".*?<div class="caption-blk">\s*).*?(</div>\s*</div>\s*</div>\s*<div class="post-actions-below">)', lambda m: m.group(1) + caption_2 + '\n      ' + m.group(2), html, flags=re.DOTALL)
html = re.sub(r'(<section class="post-section" id="sec-3".*?<div class="caption-blk">\s*).*?(</div>\s*</div>\s*</div>\s*<div class="post-actions-below">)', lambda m: m.group(1) + caption_3 + '\n      ' + m.group(2), html, flags=re.DOTALL)


with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update JS postMeta
with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_postMeta = """  const postMeta = {
    '1': { 
      caption: '<strong>[Carrossel] Apresentação</strong>', 
      cards: [
        'Antes de ser médica, fui engenheira, você sabia? Como a vida não é linear...',
        'Eu também sou paciente e há algumas coisas que me incomodam fortemente...',
        'O que você vai encontrar comigo? Uma consulta com começo, meio e fim...',
        'A educação é parte fundamental do meu cuidado...',
        'Me chamo Cláudia Mattana. Sou ginecologista...'
      ] 
    },
    '2': { caption: '<strong>[Carrossel] Posicionamento</strong><br>Você já saiu de uma consulta ginecológica com mais dúvidas do que entrou?', cards: [] },
    '3': { caption: '<strong>[Imagem Única] Locais de atendimento</strong><br>Conheça meus locais de atendimento...', cards: [] }
  };"""

js = re.sub(r'const postMeta = \{.*?\n  \};', new_postMeta, js, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Applied new copy!")
