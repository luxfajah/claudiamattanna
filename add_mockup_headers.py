import re

html_file = '/Users/luxfajah/claudia_mattanna/junho.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

def insert_header(match):
    track_id = match.group(1)
    if track_id == '1':
        date = "11 de Junho"
    elif track_id == '2':
        date = "18 de Junho"
    else:
        date = "25 de Junho"
    
    header_html = f'''<div class="ig-mock-header">
            <div class="ig-mock-left">
              <img src="foto.jpg" class="ig-mock-ava" alt="Claudia">
              <div class="ig-mock-info">
                <span class="ig-mock-name">claudiamattanna</span>
                <span class="ig-mock-date">{date}</span>
              </div>
            </div>
            <span class="material-symbols-outlined ig-mock-more">more_horiz</span>
          </div>\n          '''
    
    return f'<div class="ig-carousel">\n          {header_html}<div class="ig-track" id="itrack-{track_id}"'

html = re.sub(r'<div class="ig-carousel">\s*<div class="ig-track" id="itrack-(\d+)"', insert_header, html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)


# Update CSS
css_file = '/Users/luxfajah/claudia_mattanna/junho.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

mockup_css = """
/* Instagram Mockup Header */
.ig-mock-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 14px; border-bottom: 1px solid rgba(0,0,0,0.06);
  background: #FFF; z-index: 10; position: relative; height: 56px;
  box-sizing: border-box;
}
.ig-mock-left { display: flex; align-items: center; gap: 10px; }
.ig-mock-ava { width: 32px; height: 32px; border-radius: 50%; object-fit: cover; border: 1px solid rgba(0,0,0,0.05); }
.ig-mock-info { display: flex; flex-direction: column; line-height: 1.2; text-align: left; }
.ig-mock-name { font-weight: 600; font-size: 13px; color: #262626; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
.ig-mock-date { font-size: 11px; color: #8E8E8E; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;}
.ig-mock-more { color: #262626; font-size: 20px; }
"""

# Modify the track height from 100% to calc(100% - 56px)
css = css.replace(
    """height: 100% !important;
  width: 100% !important;""",
    """height: calc(100% - 56px) !important;
  width: 100% !important;"""
)

css += mockup_css

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Mockup headers injected!")
