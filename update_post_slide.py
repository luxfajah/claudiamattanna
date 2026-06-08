import re

# 1. Update CSS
with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r"(\.posts-horizontal-track\s*\{[^}]*)gap:\s*100px;",
    r"\1gap: 4vw; padding: 0 7.5vw;",
    css
)

css = re.sub(
    r"(\.post-section\s*\{[^}]*)min-width:\s*100vw;([^}]*)padding:\s*20px;",
    r"\1min-width: 85vw;\2padding: 20px 0;",
    css
)

# Add scale logic
scale_css = """
.post-split {
  transform: scale(0.85); opacity: 0.4;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease;
  will-change: transform, opacity;
}
.post-section.active-slide .post-split {
  transform: scale(1); opacity: 1;
}
"""
css += scale_css

# Update indicator
css = re.sub(
    r"\.post-indicator\s*\{[^}]*\}",
    """
.post-indicator {
  position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%);
  display: flex; align-items: center; gap: 6px; z-index: 50;
  background: rgba(255, 255, 255, 0.5); backdrop-filter: blur(24px) saturate(200%); -webkit-backdrop-filter: blur(24px) saturate(200%);
  border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 100px; padding: 6px 8px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}
""",
    css
)

css = re.sub(
    r"\.pi-item\s*\{[^}]*\}",
    """
.pi-item {
  font-family: var(--font-main); font-size: 13px; font-weight: 600; color: rgba(28, 43, 54, 0.6); padding: 4px 12px; border-radius: 100px; cursor: pointer; transition: all 0.3s;
}
""",
    css
)

css = re.sub(
    r"\.pi-item\.active\s*\{[^}]*\}",
    """
.pi-item.active {
  background: #007AFF; color: #fff; box-shadow: 0 2px 8px rgba(0,122,255,0.3);
}
.pi-item:not(.active):hover { color: rgba(28, 43, 54, 1); }
""",
    css
)

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update JS
with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace initIndicator
new_js = """
// Attach scroll listener
(function initIndicator() {
  const slides = document.querySelectorAll('.post-section');
  if (slides.length === 0) { setTimeout(initIndicator, 200); return; }
  
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('active-slide');
        const idx = Array.from(slides).indexOf(e.target);
        updatePostIndicator(idx);
      } else {
        e.target.classList.remove('active-slide');
      }
    });
  }, { threshold: 0.55, root: document.getElementById("mainPostsTrack") });

  slides.forEach(s => obs.observe(s));
})();
"""

js = re.sub(r"// Attach scroll listener\n\(function initIndicator\(\).*?\}\)\(\);", new_js, js, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Slide improved!")
