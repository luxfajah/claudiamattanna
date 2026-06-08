import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix dashboard header width to match post-split perfectly
css = re.sub(
    r"\.dashboard-header\s*\{[^}]*\}",
    """
.dashboard-header {
  padding: 40px 0; width: 100%; max-width: 1200px; margin: 0 auto;
}
""",
    css
)

css = re.sub(
    r"\.dh-container\s*\{[^}]*\}",
    """
.dh-container {
  display: flex; justify-content: space-between; align-items: stretch; gap: 40px;
  background: rgba(255,255,255,0.06); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255,255,255,0.1); border-radius: 32px; padding: 40px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.15);
  width: 100%; max-width: 1200px; margin: 0 auto;
}
""",
    css
)

# Fix overview split to match
css = re.sub(
    r"\.overview-split\s*\{[^}]*\}",
    """
.overview-split {
  display: grid; grid-template-columns: 320px 1fr; gap: 40px;
  width: 100%; max-width: 1200px; margin: 0 auto;
}
""",
    css
)

# Fix post-split to ensure it has exact same bounds
css = re.sub(
    r"\.post-split\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*minmax\(320px,\s*1fr\)\s*minmax\(320px,\s*1\.2fr\);\s*gap:\s*40px;\s*width:\s*100%;\s*max-width:\s*1200px;\s*margin:\s*0\s*auto;\s*align-items:\s*stretch;\s*height:\s*calc\(100vh\s*-\s*160px\);\s*max-height:\s*850px;\s*min-height:\s*600px;\s*\}",
    """
.post-split {
  display: grid; grid-template-columns: minmax(320px, 1fr) minmax(320px, 1.2fr); gap: 40px;
  width: 100%; max-width: 1200px;
  margin: 0 auto; align-items: stretch;
  height: calc(100vh - 160px); max-height: 850px; min-height: 600px;
}
""",
    css
)

# Fix metric-box flex behavior so text doesn't break
css = re.sub(
    r"\.metric-box\s*\{[^}]*\}",
    """
.metric-box {
  background: rgba(0,0,0,0.15); border-radius: 20px; padding: 20px;
  display: flex; align-items: flex-start; gap: 12px; flex: 1;
  white-space: nowrap; /* Impede a quebra de texto nas labels pequenas */
}
""",
    css
)

css = re.sub(
    r"\.dh-prog-count\s*\{[^}]*\}",
    """
.dh-prog-count { font-size: 13px; font-weight: 800; color: var(--text); white-space: nowrap; }
""",
    css
)

css = re.sub(
    r"\.btn-clear\s*\{[^}]*\}",
    """
.btn-clear {
  background: transparent; border: none; color: var(--text); opacity: 0.5; font-size: 11px;
  font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; cursor: pointer; text-align: left;
  transition: opacity 0.2s; display: inline-flex; align-items: center; gap: 4px;
  white-space: nowrap; /* Impede a quebra no botão limpar */
}
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Grid aligned and text wrapped fixed!")
