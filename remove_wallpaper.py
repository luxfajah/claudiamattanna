import re
import os

def clean_html(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the script that injects background images
    html = re.sub(r'<script>\s*\(function\(\)\s*\{\s*// Background rotation logic.*?\}\)\(\);\s*</script>', '', html, flags=re.DOTALL)
    
    # Alternatively, if the script is not exactly as above, let's catch it more broadly:
    html = re.sub(r'<script>\s*\(function\(\)\s*\{\s*try\s*\{\s*let\s+idx\s*=\s*localStorage\.getItem\(\'cm_bg_idx\'\);.*?</script>', '', html, flags=re.DOTALL)

    # Remove any `<div class="hero-bg" id="parallaxBg"></div>`
    html = re.sub(r'<div class="hero-bg" id="parallaxBg"></div>', '', html)
    html = re.sub(r'<div class="hero-bg"></div>', '', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

clean_html('/Users/luxfajah/claudia_mattanna/junho.html')
clean_html('/Users/luxfajah/claudia_mattanna/index.html')
clean_html('/Users/luxfajah/claudia_mattanna/v1.html')

print("Wallpapers completely removed from JS and HTML!")
