import re

gradient_css = """
@keyframes fluidGradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

body {
  font-family: 'Inter', -apple-system, sans-serif;
  /* Degradê 3 cores: Marinho, Celeste e Bebê */
  background: linear-gradient(-45deg, #001F3F, #4A90E2, #b3e5fc);
  background-size: 300% 300%;
  animation: fluidGradient 24s ease infinite;
  background-attachment: fixed;
  color: var(--text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  min-height: 100vh;
}
"""

def apply_universal_bg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it's a CSS file, we just replace the body block
    # If it's an HTML file, we replace the body block inside <style>
    if content.find('@keyframes fluidGradient') == -1:
        # inject the keyframes just before body
        content = re.sub(r"body\s*\{[^}]*\}", gradient_css, content, count=1)
    else:
        # replace the existing one
        content = re.sub(r"@keyframes fluidGradient\s*\{[^}]*\}\s*body\s*\{[^}]*\}", gradient_css.strip(), content, count=1)

    # Clean up index.html specific overrides
    if filepath.endswith('index.html'):
        # Make login screen glass over the gradient
        content = re.sub(
            r"\.login-screen\s*\{[^}]*background:\s*#111;[^}]*\}",
            """
.login-screen {
  position: fixed; inset: 0; z-index: 9999;
  display: flex; align-items: center; justify-content: center;
  background: rgba(255,255,255,0.05); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  transition: opacity .8s;
}
""",
            content
        )
        # Remove any ::before pseudo element holding bg.jpg
        content = re.sub(r"\.login-screen::before\s*\{[^}]*\}", "", content)
        content = re.sub(r"\.hero-bg\s*\{[^}]*\}", "", content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

apply_universal_bg('/Users/luxfajah/claudia_mattanna/junho.css')
apply_universal_bg('/Users/luxfajah/claudia_mattanna/index.html')

print("Universal 3-color gradient applied to both pages!")
