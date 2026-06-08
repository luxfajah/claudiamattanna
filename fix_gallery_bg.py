import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the gallery background white
css = re.sub(
    r"\.gallery-col \.ig-carousel\s*\{[^}]*\}",
    """
.gallery-col .ig-carousel {
  width: 100%; height: 100%; position: relative; border-radius: 24px; overflow: hidden;
  background: #FFFFFF; /* Makes the space around contain images white */
  box-shadow: 0 16px 40px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.4);
}
""",
    css
)

# Move the post-indicator to the top
css = re.sub(
    r"\.post-indicator\s*\{\s*position:\s*absolute;\s*bottom:\s*30px;",
    ".post-indicator { position: absolute; top: 30px; bottom: auto;",
    css
)

# We should do a global replace just in case there are multiple
css = css.replace("bottom: 30px; left: 50%;", "top: 30px; left: 50%;")

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Gallery bg and indicator fixed!")
