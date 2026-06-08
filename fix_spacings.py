import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix image vertical centering inside the white gallery box
css = re.sub(
    r"\.ig-slide\s*\{\s*min-width:\s*100%;\s*position:\s*relative;\s*\}",
    """
.ig-slide {
  min-width: 100%; position: relative;
  display: flex; align-items: center; justify-content: center; /* Centers the image vertically */
}
""",
    css
)

# Push the post indicator up and fix its position
css = re.sub(
    r"\.post-indicator\s*\{[^}]*\}",
    """
.post-indicator {
  position: absolute; top: 24px; left: 50%; transform: translateX(-50%);
  display: flex; align-items: center; gap: 6px; z-index: 100;
  background: rgba(255, 255, 255, 0.5); backdrop-filter: blur(24px) saturate(200%); -webkit-backdrop-filter: blur(24px) saturate(200%);
  border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 100px; padding: 6px 8px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}
""",
    css
)

# Add padding to post-section to guarantee it never hits the indicator
css = re.sub(
    r"\.post-section\s*\{\s*min-width:\s*85vw;\s*height:\s*100%;\s*scroll-snap-align:\s*center;\s*scroll-snap-stop:\s*always;\s*display:\s*flex;\s*flex-direction:\s*column;\s*align-items:\s*center;\s*justify-content:\s*center;\s*\}",
    """
.post-section {
  min-width: 85vw; height: 100%; scroll-snap-align: center; scroll-snap-stop: always;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding-top: 40px; /* guarantees space for the indicator */
}
""",
    css
)

# Adjust dots spacing
css = re.sub(
    r"\.ig-carousel-dots\s*\{[^}]*\}",
    """
.ig-carousel-dots {
  position: absolute; bottom: 24px; left: 0; width: 100%;
  display: flex; justify-content: center; gap: 6px; z-index: 10;
}
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Spacings fixed!")
