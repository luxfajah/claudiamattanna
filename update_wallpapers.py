import re

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The script to inject right after <style> or before </head>
inline_script = """  <script>
    (function(){
      // Cycle through 1, 2, 3
      let idx = localStorage.getItem('cm_bg_idx');
      idx = idx ? parseInt(idx) : 1;
      idx = idx > 3 ? 1 : idx;
      
      const nextIdx = idx >= 3 ? 1 : idx + 1;
      localStorage.setItem('cm_bg_idx', nextIdx);
      
      const bgUrl = `bg${idx}.jpg`;
      
      // Inject CSS variables so that preloader and hero-bg can use it immediately
      document.write(`<style>
        :root { --current-bg: url('${bgUrl}'); }
        .hero-bg { background: var(--current-bg) center/cover no-repeat !important; filter: saturate(1.1) brightness(0.85); }
        .preloader { background: var(--current-bg) center/cover no-repeat !important; }
        .preloader::before { content: ''; position: absolute; inset: 0; background: rgba(255,255,255,0.7); backdrop-filter: blur(10px); }
        .preloader-content { position: relative; z-index: 2; }
      </style>`);
    })();
  </script>
</head>"""

# Replace </head> with the inline script
html = html.replace('</head>', inline_script)

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated wallpapers script injected!")
