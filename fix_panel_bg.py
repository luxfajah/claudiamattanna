import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make .post-panel solid and structured
css = re.sub(
    r"\.post-panel\s*\{\s*display:\s*flex\s*!important;\s*flex-direction:\s*column\s*!important;\s*height:\s*100%\s*!important;\s*overflow:\s*hidden\s*!important;\s*\}",
    """
.post-panel {
  display: flex !important; flex-direction: column !important; 
  height: 100% !important; overflow: hidden !important; 
  background: #FFFFFF !important;
  border-radius: 24px !important;
  padding: 32px !important;
  box-shadow: 0 16px 40px rgba(0,0,0,0.1) !important;
}
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Solid background added to .post-panel!")
