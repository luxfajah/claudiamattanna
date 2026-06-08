import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

header_css = """
/* ════════════════════════ DASHBOARD HEADER ════════════════════════ */
.dashboard-header {
  position: relative;
  z-index: 10;
  padding: 60px 5vw 40px 5vw;
  display: flex;
  justify-content: center;
}

.dh-container {
  width: 100%;
  max-width: 1200px;
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(40px) saturate(200%);
  -webkit-backdrop-filter: blur(40px) saturate(200%);
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-radius: 32px;
  padding: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 20px 40px rgba(0,0,0,0.05);
  gap: 40px;
}

.dh-client {
  display: flex;
  align-items: center;
  gap: 24px;
}

.dh-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  border: 3px solid #fff;
  flex-shrink: 0;
}

.dh-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.dh-titles {
  display: flex;
  flex-direction: column;
}

.dh-eyebrow {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: rgba(0,0,0,0.4);
  font-weight: 700;
  margin-bottom: 8px;
}

.dh-name {
  font-family: var(--font-head);
  font-size: 36px;
  font-weight: 300;
  color: var(--text);
  margin: 0 0 4px 0;
  line-height: 1.1;
}

.dh-tagline {
  font-size: 15px;
  color: rgba(0,0,0,0.6);
  margin: 0;
}

.dh-metrics {
  display: flex;
  gap: 32px;
  align-items: center;
}

.metric-box {
  display: flex;
  align-items: center;
  gap: 12px;
}

.m-icon {
  font-size: 24px;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.04);
  border-radius: 14px;
}

.m-text {
  display: flex;
  flex-direction: column;
}

.m-label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(0,0,0,0.4);
  font-weight: 600;
  margin-bottom: 2px;
}

.m-val {
  font-size: 14px;
  color: var(--text);
  font-weight: 500;
}

.dh-progress-box {
  background: #fff;
  border-radius: 20px;
  padding: 16px 24px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 220px;
}

.dh-progress-texts {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dh-prog-label {
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
}

.dh-prog-count {
  font-size: 12px;
  color: rgba(0,0,0,0.5);
  font-weight: 500;
}

.dh-pb-track {
  width: 100%;
  height: 6px;
  background: rgba(0,0,0,0.06);
  border-radius: 10px;
  overflow: hidden;
}

.dh-pb-fill {
  height: 100%;
  background: var(--accent, #108A58);
  border-radius: 10px;
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-clear {
  background: none;
  border: none;
  font-size: 11px;
  color: rgba(0,0,0,0.4);
  cursor: pointer;
  text-align: left;
  padding: 0;
  font-weight: 500;
  transition: color 0.2s;
}

.btn-clear:hover {
  color: #B31919;
}

@media (max-width: 1000px) {
  .dh-container {
    flex-direction: column;
    align-items: flex-start;
  }
  .dh-metrics {
    flex-wrap: wrap;
    width: 100%;
  }
}
"""

css += header_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Dashboard header CSS injected!")
