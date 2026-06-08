import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update main post-split grid to be height-constrained
css = re.sub(
    r"\.post-split\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*minmax\(320px,\s*1fr\)\s*minmax\(320px,\s*1\.2fr\);\s*gap:\s*40px;\s*width:\s*100%;\s*max-width:\s*1200px;\s*margin:\s*0\s*auto;\s*align-items:\s*start;\s*\}",
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

# Constrain gallery height
css = re.sub(
    r"\.gallery-col\s*\{[^}]*\}",
    """
.gallery-col {
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  background: transparent; border-radius: 24px; overflow: hidden; position: relative;
  width: 100%; height: 100%;
}
""",
    css
)

css = re.sub(
    r"\.gallery-col \.ig-carousel\s*\{[^}]*\}",
    """
.gallery-col .ig-carousel {
  width: 100%; height: 100%; position: relative; border-radius: 24px; overflow: hidden;
  box-shadow: 0 16px 40px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.4);
}
""",
    css
)

css = re.sub(
    r"\.gallery-col \.ig-slide img\s*\{[^}]*\}",
    """
.gallery-col .ig-slide img {
  width: 100%; height: 100%; object-fit: contain; display: block;
}
""",
    css
)

# Append height constraints to post-panel and caption-blk so the buttons never get pushed out
css += """

/* Height overrides to prevent overflow */
.post-panel {
  display: flex !important; flex-direction: column !important; 
  height: 100% !important; overflow: hidden !important; 
}
.post-panel .post-head {
  flex-shrink: 0;
}
.post-panel .blk-label {
  flex-shrink: 0;
}
.caption-blk {
  flex: 1 1 auto !important; overflow-y: auto !important; margin-bottom: 0 !important; 
  padding-right: 16px !important;
}
.caption-blk::-webkit-scrollbar { width: 6px; }
.caption-blk::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.15); border-radius: 10px; }
.panel-actions-wrapper {
  flex-shrink: 0; margin-top: 24px !important;
}

@media(max-width: 900px) {
  .post-split {
    height: auto !important; max-height: none !important; min-height: 0 !important;
    align-items: start !important;
  }
  .gallery-col { height: auto !important; }
  .gallery-col .ig-carousel { height: auto !important; aspect-ratio: 1/1; }
  .gallery-col .ig-slide img { object-fit: cover !important; }
  .post-panel { height: auto !important; overflow: visible !important; }
  .caption-blk { overflow-y: visible !important; flex: none !important; }
}
"""

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Heights constrained!")
