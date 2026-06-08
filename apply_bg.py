import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_body = """
@keyframes fluidGradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

body {
  font-family: var(--font-main);
  background: linear-gradient(-45deg, #B8CDD6, #6b9eb8, #2C3E4A);
  background-size: 300% 300%;
  animation: fluidGradient 20s ease infinite;
  background-attachment: fixed;
  color: var(--text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  min-height: 100vh;
}
"""

# Replace existing body
css = re.sub(r"body\s*\{[^}]*\}", new_body, css, count=1)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Gradient background applied!")
