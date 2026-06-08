import re

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_fixes = """
/* ════════════════════════ MOBILE LAYOUT FIXES ════════════════════════ */
@media (max-width: 900px) {
  /* 1. Reset the absolute section paddings to allow scrolling instead of overlapping */
  .post-section { 
    height: auto !important; 
    padding-top: 80px !important; 
    padding-bottom: 24px !important;
    scroll-snap-align: start !important;
  }
  
  .post-indicator {
    top: 20px !important;
  }

  /* 2. Unconstrain the split grid height so it can stack naturally */
  .post-split { 
    height: auto !important; 
    max-height: none !important; 
    min-height: auto !important; 
    grid-template-columns: 1fr !important;
  }

  /* 3. Flip the carousel from Height-bound to Width-bound */
  .gallery-col {
    height: auto !important;
  }
  .gallery-col .ig-carousel {
    width: 100% !important;
    max-width: 500px !important;
    height: auto !important;
  }
  .gallery-col .ig-track {
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 4 / 5 !important;
  }

  /* 4. Dashboard Header refinements for mobile */
  .dashboard-header {
    padding: 32px 5vw 24px 5vw !important;
  }
  .dh-container {
    padding: 24px !important;
    gap: 24px !important;
    flex-direction: column !important;
    align-items: center !important;
  }
  .dh-client {
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
  }
  .dh-name {
    font-size: 28px !important;
  }
  .dh-metrics {
    justify-content: center !important;
    gap: 16px !important;
  }
  .dh-progress-box {
    width: 100% !important;
    box-sizing: border-box !important;
  }
  
  /* 5. Final Dashboard Mobile Fixes */
  .final-dashboard-section {
    margin: 40px 0 60px 0 !important;
  }
}
"""

css += mobile_fixes

with open('/Users/luxfajah/claudia_mattanna/junho.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Mobile layouts fixed!")
