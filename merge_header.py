import re

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

dashboard_html = """
<header class="dashboard-header reveal">
  <div class="dh-container">
    
    <!-- Esquerda: Identidade -->
    <div class="dh-client">
      <div class="dh-avatar">
        <img src="foto.jpg" alt="Claudia Mattanna">
      </div>
      <div class="dh-titles">
        <div class="dh-eyebrow">Planejamento de conteúdo · Junho</div>
        <h1 class="dh-name">Claudia Mattanna</h1>
        <p class="dh-tagline">Revise, comente e aprove as peças abaixo.</p>
      </div>
    </div>

    <!-- Direita: Resumo (Foco, Status, Prazo) -->
    <div class="dh-metrics">
      <div class="metric-box">
        <div class="m-icon">📋</div>
        <div class="m-text">
          <span class="m-label">Foco da Campanha</span>
          <span class="m-val">Apresentação e Posicionamento</span>
        </div>
      </div>
      <div class="metric-box">
        <div class="m-icon">⏰</div>
        <div class="m-text">
          <span class="m-label">Prazo de Resposta</span>
          <span class="m-val">Em aberto</span>
        </div>
      </div>
      
      <!-- Barra de Progresso Integrada -->
      <div class="dh-progress-box">
        <div class="dh-progress-texts">
          <span class="dh-prog-label">Progresso</span>
          <span class="dh-prog-count" id="infoCount">0 de 3 aprovados</span>
        </div>
        <div class="dh-pb-track">
          <div class="dh-pb-fill" id="infoFill" style="width:0%"></div>
        </div>
        <button class="btn-clear" onclick="clearState()"><span class="material-symbols-outlined" style="font-size:14px; vertical-align:text-bottom;">refresh</span> Limpar Sessão</button>
      </div>
    </div>
    
  </div>
  
  <!-- Dummy elements to prevent JS errors since we removed the double bars -->
  <div style="display:none;">
    <div id="pbFill"></div>
    <div id="pbLabel"></div>
  </div>
</header>
"""

# Regex to remove from <section class="hero" id="heroSec"> up to </section> of infoPanelSection
pattern = r'<section class="hero" id="heroSec">.*?</section>\s*<!-- ════════════════════════ INFO PANEL \(SEC: 2\) ════════════════════════ -->\s*<section id="infoPanelSection" class="info-container">.*?</section>'

html = re.sub(pattern, dashboard_html, html, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

dashboard_css = """
/* ── Dashboard Header (Merged) ── */
.dashboard-header {
  padding: 40px 16px; width: 100%; max-width: 1200px; margin: 0 auto;
}
.dh-container {
  display: flex; justify-content: space-between; align-items: stretch; gap: 40px;
  background: rgba(255,255,255,0.06); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255,255,255,0.1); border-radius: 32px; padding: 40px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.15);
}

.dh-client {
  display: flex; align-items: center; gap: 24px; flex: 1;
}
.dh-avatar {
  width: 90px; height: 90px; border-radius: 50%; overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2); flex-shrink: 0;
  border: 2px solid rgba(255,255,255,0.3);
}
.dh-avatar img { width: 100%; height: 100%; object-fit: cover; }
.dh-titles { display: flex; flex-direction: column; justify-content: center; }
.dh-eyebrow { font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.7); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 6px; }
.dh-name { font-family: 'Fraunces', serif; font-size: 32px; font-weight: 300; color: #fff; margin: 0 0 8px 0; line-height: 1.1; }
.dh-tagline { font-size: 14px; color: rgba(255,255,255,0.8); margin: 0; }

.dh-metrics {
  display: flex; gap: 24px; flex: 1; align-items: stretch;
}
.metric-box {
  background: rgba(0,0,0,0.15); border-radius: 20px; padding: 20px;
  display: flex; align-items: flex-start; gap: 12px; flex: 1;
}
.m-icon { font-size: 24px; }
.m-text { display: flex; flex-direction: column; gap: 4px; }
.m-label { font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.6); text-transform: uppercase; letter-spacing: 0.05em; }
.m-val { font-size: 13px; color: #fff; line-height: 1.4; font-weight: 500; }

.dh-progress-box {
  background: rgba(255,255,255,0.9); border-radius: 20px; padding: 20px;
  flex: 1; display: flex; flex-direction: column; justify-content: center;
}
.dh-progress-texts {
  display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;
}
.dh-prog-label { font-size: 11px; font-weight: 700; color: var(--text); text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.6; }
.dh-prog-count { font-size: 13px; font-weight: 800; color: var(--text); }
.dh-pb-track {
  width: 100%; height: 6px; background: rgba(0,0,0,0.06); border-radius: 10px; overflow: hidden; margin-bottom: 12px;
}
.dh-pb-fill {
  height: 100%; background: var(--accent); border-radius: 10px; transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.btn-clear {
  background: transparent; border: none; color: var(--text); opacity: 0.5; font-size: 11px;
  font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; cursor: pointer; text-align: left;
  transition: opacity 0.2s; display: inline-flex; align-items: center; gap: 4px;
}
.btn-clear:hover { opacity: 1; color: var(--rose); }

@media(max-width: 1000px) {
  .dh-container { flex-direction: column; }
  .dh-metrics { flex-direction: column; }
  .dashboard-header { padding: 20px 16px; }
}
"""

css += dashboard_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Dashboard Header implemented!")
