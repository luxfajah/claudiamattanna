import re

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the IG Carousel logic
ig_logic_pattern = r"/\* ── IG Carousel ─────────────────────────────────────── \*/.*?/\* ── Status & actions ─────────────────────────────────── \*/"

new_ig_logic = """/* ── IG Carousel ─────────────────────────────────────── */
  const ig = {};
  function initIG(id){
    const t = document.getElementById(`itrack-${id}`);
    if(!t) return;
    const n = t.children.length;
    ig[id] = {i:0, n};
    const dc = document.getElementById(`idots-${id}`);
    if(dc) {
      dc.innerHTML = '';
      for(let x=0;x<n;x++){
        const d = document.createElement('div');
        d.className = 'ig-dot'+(x===0?' active':'');
        dc.appendChild(d);
      }
    }
    
    // Sync dots when user swipes natively
    t.addEventListener('scroll', () => {
      const idx = Math.round(t.scrollLeft / t.clientWidth);
      ig[id].i = idx;
      if(dc) {
        [...dc.children].forEach((d,i)=>d.classList.toggle('active', i===idx));
      }
    }, {passive: true});
  }
  
  function igSlide(id,dir){
    const s = ig[id]; if(!s) return;
    const ni = s.i + dir;
    if(ni<0||ni>=s.n) return;
    
    const track = document.getElementById(`itrack-${id}`);
    const slideWidth = track.clientWidth;
    track.scrollTo({ left: ni * slideWidth, behavior: 'smooth' });
  }
  
  // Initialize all 3 carousels
  ['1','2','3'].forEach(initIG);

  /* ── Status & actions ─────────────────────────────────── */"""

js = re.sub(ig_logic_pattern, new_ig_logic, js, flags=re.DOTALL)

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS Carousel Logic Fixed!")
