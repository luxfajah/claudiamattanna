import re

# 1. Update HTML
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find everything from DOWNLOADS up to the end of the footer
old_blocks_pattern = r"<!-- ════════════════════════ DOWNLOADS ════════════════════════ -->.*?</footer>"

new_html = """<!-- ════════════════════════ FINAL DASHBOARD ════════════════════════ -->
<section class="final-dashboard-section" style="margin: 80px 0 120px 0; padding: 0 5vw;">
  <div class="post-split" style="height: auto; min-height: auto; max-height: none;">
    
    <!-- LEFT: DOWNLOADS -->
    <div class="post-panel" style="padding: 40px; display: flex; flex-direction: column; justify-content: center; height: 100%;">
      <h2 style="font-family: var(--font-head); font-size: 32px; color: var(--text); margin-bottom: 8px;">Arquivos Originais</h2>
      <p style="color: rgba(0,0,0,0.6); margin-bottom: 32px; font-size: 14px;">Baixe as artes em alta qualidade para publicar no seu Instagram.</p>
      
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <a href="#" class="abtn btn-pri" style="width: 100%; justify-content: center; margin-bottom: 16px;"><span class="material-symbols-outlined">folder_zip</span> Baixar Pasta Completa</a>
        
        <a href="#" class="dl-item">
          <div class="dl-icon">01</div>
          <div class="dl-text">Post 1 — Carrossel</div>
          <span class="material-symbols-outlined">download</span>
        </a>
        <a href="#" class="dl-item">
          <div class="dl-icon">02</div>
          <div class="dl-text">Post 2 — Carrossel</div>
          <span class="material-symbols-outlined">download</span>
        </a>
        <a href="#" class="dl-item">
          <div class="dl-icon">03</div>
          <div class="dl-text">Post 3 — Imagem Única</div>
          <span class="material-symbols-outlined">download</span>
        </a>
      </div>
    </div>

    <!-- RIGHT: OBRIGADA & RESUMO -->
    <div class="post-panel" style="padding: 40px; display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
      <div>
        <h2 style="font-family: var(--font-head); font-size: 40px; color: var(--text); margin-bottom: 16px; line-height: 1;">Obri<em>gada!</em></h2>
        <p style="color: rgba(0,0,0,0.6); line-height: 1.6; font-size: 15px;">Fique à vontade para enviar qualquer feedback adicional. Isso nos ajuda a evoluir cada detalhe do seu projeto e entregar o melhor resultado possível.</p>
      </div>
      
      <div style="margin-top: 40px;">
        <h3 style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(0,0,0,0.4); margin-bottom: 16px;">Resumo da Aprovação</h3>
        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
          <div class="summary-pill approved-pill">
            <span class="sp-num" id="f-approved">0</span>
            <span class="sp-lbl">Aprovados</span>
          </div>
          <div class="summary-pill pending-pill">
            <span class="sp-num" id="f-pending">3</span>
            <span class="sp-lbl">Pendentes</span>
          </div>
          <div class="summary-pill rejected-pill">
            <span class="sp-num" id="f-rejected">0</span>
            <span class="sp-lbl">Reprovados</span>
          </div>
        </div>
      </div>
      
      <div style="margin-top: 40px; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 24px; font-size: 13px; color: rgba(0,0,0,0.4);">
        Criado com cuidado pela <strong>Duas Mãos.</strong>
      </div>
    </div>
    
  </div>
</section>"""

html = re.sub(old_blocks_pattern, new_html, html, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* ── FINAL DASHBOARD ── */
.dl-item {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 20px; background: rgba(0,0,0,0.03); border-radius: 16px;
  color: var(--text); text-decoration: none; font-size: 14px; font-weight: 500;
  transition: all 0.2s ease;
}
.dl-item:hover { background: rgba(0,0,0,0.06); transform: scale(0.99); }
.dl-item .dl-icon { font-family: var(--font-head); font-size: 16px; color: rgba(0,0,0,0.4); width: 24px; }
.dl-item .dl-text { flex: 1; }
.dl-item .material-symbols-outlined { color: rgba(0,0,0,0.4); }

.summary-pill {
  flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 24px 16px; border-radius: 20px; background: rgba(0,0,0,0.03); min-width: 90px;
}
.summary-pill.approved-pill { background: rgba(22, 196, 127, 0.1); color: #108A58; }
.summary-pill.pending-pill { background: rgba(245, 166, 35, 0.1); color: #B37400; }
.summary-pill.rejected-pill { background: rgba(255, 75, 75, 0.1); color: #B31919; }

.summary-pill .sp-num { font-family: var(--font-head); font-size: 32px; font-weight: 400; line-height: 1; margin-bottom: 8px; }
.summary-pill .sp-lbl { font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; font-weight: 600; }
"""

css += new_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Dashboard footer injected!")
