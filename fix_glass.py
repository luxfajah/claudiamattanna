import re

hero_overlay_css = """.hero-overlay {
  display: block;
  position: absolute; inset: 0;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  background: linear-gradient(180deg, rgba(28, 43, 54, 0.5) 0%, transparent 100%);
  mask-image: linear-gradient(to bottom, black 0%, black 30%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 0%, black 30%, transparent 100%);
}"""

# Update junho.css
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'\.hero-overlay\s*\{[^}]*\}', hero_overlay_css, css)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.html hero-overlay
with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = re.sub(
    r'\.hero-overlay\s*\{[^}]*\}',
    hero_overlay_css,
    index_html
)

with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Update junho.html preloader
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    junho_html = f.read()

preloader_css = """.preloader::before { content: ''; position: absolute; inset: 0; background: rgba(28, 43, 54, 0.4); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }
        .preloader::after { content: ''; position: absolute; inset: 0; opacity: .04; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); background-size: 200px; z-index: -1; }"""

# The inline style currently has:
# .preloader::before { content: ''; position: absolute; inset: 0; background: rgba(28, 43, 54, 0.85); backdrop-filter: blur(10px); }
junho_html = re.sub(
    r'\.preloader::before\s*\{[^}]*\}',
    preloader_css,
    junho_html
)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(junho_html)

print("Glass effects applied!")
