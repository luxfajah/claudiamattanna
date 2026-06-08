import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Force height 100% and flex-basis 100% on track and slides so they never collapse or shrink
override_css = """
/* ── CRITICAL CAROUSEL DIMENSIONS FIX ── */
.ig-track, .gallery-col .ig-track {
  height: 100% !important;
  width: 100% !important;
}

.ig-slide, .gallery-col .ig-slide {
  height: 100% !important;
  flex: 0 0 100% !important; /* Prevents flex shrinking when swiping */
  min-width: 100% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  position: relative !important;
}

.ig-slide img, .gallery-col .ig-slide img {
  height: 100% !important;
  width: 100% !important;
  object-fit: contain !important;
  display: block !important;
}
"""

css += override_css

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Carousel dimensions fixed!")
