import re

css_file = '/Users/luxfajah/claudia_mattanna/junho.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Make the white box shrink-wrap to the exact width of the 4:5 images
css = re.sub(
    r"\.gallery-col \.ig-carousel\s*\{[^}]*\}",
    """
.gallery-col .ig-carousel {
  height: 100%; position: relative; border-radius: 24px; overflow: hidden;
  background: #FFFFFF;
  box-shadow: 0 16px 40px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.4);
  width: fit-content; margin: 0 auto; /* Shrink to fit the 4:5 track */
}
""",
    css
)

# Force the track to be exactly 4:5
css = css.replace(
    """  height: calc(100% - 56px) !important;
  width: 100% !important;""",
    """  height: calc(100% - 56px) !important;
  aspect-ratio: 4 / 5 !important;
  width: auto !important;"""
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Aspect ratio fixed!")
