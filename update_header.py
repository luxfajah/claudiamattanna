import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Header CSS
css = re.sub(
    r"\.post-head\s*\{[^}]*\}",
    """
.post-head {
  display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;
  padding-bottom: 20px; border-bottom: 1px solid rgba(0,0,0,0.06);
}
""",
    css
)

css = re.sub(
    r"\.post-title\s*\{[^}]*\}",
    """
.post-title {
  font-size: 28px; line-height: 1.1; margin: 0; color: var(--text); font-weight: 600;
}
.post-title em {
  font-weight: 300; font-family: 'Fraunces', serif; color: var(--accent); font-style: italic;
}
""",
    css
)

new_header_styles = """
.ph-top-row {
  display: flex; align-items: center; justify-content: space-between;
}
.post-eyebrow {
  display: flex; align-items: center; gap: 8px; font-size: 11px; color: rgba(0,0,0,0.4); text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;
}
.sb {
  display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 100px;
  font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;
}
"""
css += new_header_styles

# 2. Update Button Layout CSS
css = re.sub(
    r"\.panel-actions-wrapper \.actions\s*\{[^}]*\}",
    """
.panel-actions-wrapper .actions {
  display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
}
""",
    css
)

css = re.sub(
    r"\.panel-actions-wrapper \.actions-left\s*\{[^}]*\}",
    """
.panel-actions-wrapper .actions-left {
  display: contents; /* Elevates children to grid */
}
""",
    css
)

css = re.sub(
    r"\.abtn\s*\{[^}]*\}",
    """
.abtn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  padding: 16px; font-size: 14px; font-weight: 700; border-radius: 16px; cursor: pointer;
  background: rgba(0,0,0,0.03); color: var(--text); border: 1px solid rgba(0,0,0,0.08);
  transition: all 0.2s;
}
.abtn:hover { background: rgba(0,0,0,0.06); }
""",
    css
)

css = re.sub(
    r"\.abtn\.btn-ap\s*\{[^}]*\}",
    """
.abtn.btn-ap { 
  grid-column: 1 / -1; /* Full width */
  background: var(--accent); color: #fff; border: none; font-size: 16px; padding: 20px;
  box-shadow: 0 8px 24px rgba(184, 151, 90, 0.3); /* Gold shadow */
}
.abtn.btn-ap:hover { background: #a3854d; transform: translateY(-2px); }
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update HTML Header Structure
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_head(match):
    idx = match.group(1)
    type_ = match.group(2)
    date = match.group(3)
    title_num = match.group(4)
    title_text = match.group(5)
    
    return f"""<div class="post-head">
        <div class="ph-top-row">
          <div class="post-eyebrow">
            <span id="eyebrow-{idx}">{type_}</span> <span class="date">{date}</span>
          </div>
          <div class="sb sb-none" id="badge-{idx}"><span class="sbp"></span>Aguardando</div>
        </div>
        <h3 class="post-title">Peça {title_num} — <em>{title_text}</em></h3>
      </div>"""

# Match: <div class="post-head"> ... </div>
html = re.sub(
    r'<div class="post-head">\s*<div class="post-eyebrow">\s*<span id="eyebrow-(\d+)">([^<]+)</span> <span class="date">🗓([^<]+)</span>\s*<span class="v3-badge">v1</span>\s*</div>\s*<h3 class="post-title">Peça ([^—]+) — <em>([^<]+)</em></h3>\s*<div class="sb sb-none" id="badge-\d+"><span class="sbp"></span>Aguardando</div>\s*</div>',
    replace_head,
    html,
    flags=re.DOTALL
)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Header and buttons improved!")
