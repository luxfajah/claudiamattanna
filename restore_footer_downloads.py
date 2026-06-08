import re

html_to_inject = """
<!-- Modal de Erro Persistente -->
<div id="error-modal" class="error-modal">
  <div class="error-content">
    <button class="error-close" id="closeErrorModal" onclick="document.getElementById('error-modal').classList.remove('open')">&times;</button>
    <div style="font-size: 40px; margin-bottom: 15px;">⚠️</div>
    <h3 style="margin-bottom: 10px; font-family: 'Canela', serif;">Erro no Servidor</h3>
    <p style="font-size: 14px; color: #666; margin-bottom: 20px;">Não foi possível completar a ação. Por favor, copie a mensagem de erro abaixo:</p>
    <div id="error-message-text" style="background: #f8f8f8; padding: 15px; border-radius: 12px; font-family: monospace; font-size: 13px; color: #d00; margin-bottom: 20px; word-break: break-all; text-align: left; border: 1px solid #eee;"></div>
    <button class="abtn btn-ap" style="width: 100%;" onclick="document.getElementById('error-modal').classList.remove('open')">Entendido</button>
  </div>
</div>
<!-- ════════════════════════ DOWNLOADS ════════════════════════ -->
<section class="downloads-section">
  <div class="downloads-inner">
    <div class="downloads-eyebrow">📥 Arquivos originais</div>
    <h2 class="downloads-title">Baixar <em>conteúdos</em></h2>
    <div class="downloads-divider"></div>
    <div class="downloads-grid">
      <a href="#" class="dl-card dl-all" target="_blank">
        <div class="dl-icon">📁</div>
        <div class="dl-info">
          <div class="dl-label">Todos os conteúdos</div>
          <div class="dl-sub">Pasta completa</div>
        </div>
        <div class="dl-arrow">↗</div>
      </a>
      <a href="#" class="dl-card">
        <div class="dl-num">01</div>
        <div class="dl-info">
          <div class="dl-label">Post 1</div>
          <div class="dl-sub">Baixar Arquivo</div>
        </div>
        <div class="dl-arrow">↗</div>
      </a>
      <a href="#" class="dl-card">
        <div class="dl-num">02</div>
        <div class="dl-info">
          <div class="dl-label">Post 2</div>
          <div class="dl-sub">Baixar Arquivo</div>
        </div>
        <div class="dl-arrow">↗</div>
      </a>
      <a href="#" class="dl-card">
        <div class="dl-num">03</div>
        <div class="dl-info">
          <div class="dl-label">Post 3</div>
          <div class="dl-sub">Baixar Arquivo</div>
        </div>
        <div class="dl-arrow">↗</div>
      </a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="footer-bg"></div>
  <div class="footer-grain"></div>
  <div class="footer-content">
    <p class="footer-title">Obri<em>gada!</em></p>
    <div class="footer-div"></div>
    <p class="footer-body">Fique à vontade para enviar qualquer feedback adicional.<br>Isso nos ajuda a evoluir cada detalhe do seu projeto.</p>
    <div class="footer-summary">
      <div class="fs-item"><div class="fs-num green" id="f-approved">0</div><div class="fs-lbl">Aprovados</div></div>
      <div class="fs-item"><div class="fs-num yellow" id="f-pending">3</div><div class="fs-lbl">Pendentes</div></div>
      <div class="fs-item"><div class="fs-num wine" id="f-rejected">0</div><div class="fs-lbl">Reprovados</div></div>
    </div>
    <p class="footer-sig" style="margin-top:36px">Criado com cuidado pela <strong>Duas Mãos.</strong></p>
  </div>
</footer>

<div id="toast"><span class="ti" id="ti"></span><span class="tm" id="tm"></span></div>

"""

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '<!-- ════════════════════════ DOWNLOADS ════════════════════════ -->' not in html:
    html = html.replace(
        '<!-- ════════════════════════ LIGHTBOX ════════════════════════ -->',
        html_to_inject + '\n<!-- ════════════════════════ LIGHTBOX ════════════════════════ -->'
    )
    with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Downloads and footer injected!")
else:
    print("Downloads section already exists.")
