import re

with open('/Users/luxfajah/claudia_mattanna/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The script to inject right before </head>
inline_script = """  <script>
    (function(){
      // Cycle through 1, 2, 3
      let idx = localStorage.getItem('cm_bg_idx');
      idx = idx ? parseInt(idx) : 1;
      idx = idx > 3 ? 1 : idx;
      
      const nextIdx = idx >= 3 ? 1 : idx + 1;
      localStorage.setItem('cm_bg_idx', nextIdx);
      
      const bgUrl = `bg${idx}.png`;
      
      // Inject CSS variables so that login and hero-bg can use it immediately
      document.write(`<style>
        :root { --current-bg: url('${bgUrl}'); }
        .hero-bg { background: var(--current-bg) center/cover no-repeat !important; filter: blur(2px) saturate(1.1); transform: scale(1.04); }
        .login-screen::before { background: var(--current-bg) center/cover no-repeat !important; filter: blur(10px) brightness(0.6); transform: scale(1.1); }
      </style>`);
    })();
  </script>
</head>"""

if 'cm_bg_idx' not in html:
    html = html.replace('</head>', inline_script)
else:
    # already updated, so maybe just replace it if needed
    pass

with open('/Users/luxfajah/claudia_mattanna/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated wallpapers script injected in index.html!")
