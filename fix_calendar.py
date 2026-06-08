import re

# New calendar HTML for June 2026
calendar_html = """          <div class="calendar-grid">
            <!-- Week 1 -->
            <div class="calendar-day empty"></div>
            <div class="calendar-day">1</div>
            <div class="calendar-day">2</div>
            <div class="calendar-day">3</div>
            <div class="calendar-day">4</div>
            <div class="calendar-day">5</div>
            <div class="calendar-day">6</div>
            <!-- Week 2 -->
            <div class="calendar-day">7</div>
            <div class="calendar-day">8</div>
            <div class="calendar-day">9</div>
            <div class="calendar-day">10</div>
            <div class="calendar-day has-post" onclick="goToPost(0)" title="Post 1">
              <img src="Junho/Post 1 - 1.png" alt="Post 1">
              <div class="day-number">11</div>
            </div>
            <div class="calendar-day">12</div>
            <div class="calendar-day">13</div>
            <!-- Week 3 -->
            <div class="calendar-day">14</div>
            <div class="calendar-day">15</div>
            <div class="calendar-day">16</div>
            <div class="calendar-day">17</div>
            <div class="calendar-day has-post" onclick="goToPost(1)" title="Post 2">
              <img src="Junho/Post 2 - 1.png" alt="Post 2">
              <div class="day-number">18</div>
            </div>
            <div class="calendar-day">19</div>
            <div class="calendar-day">20</div>
            <!-- Week 4 -->
            <div class="calendar-day">21</div>
            <div class="calendar-day">22</div>
            <div class="calendar-day">23</div>
            <div class="calendar-day">24</div>
            <div class="calendar-day has-post" onclick="goToPost(2)" title="Post 3">
              <img src="Junho/Post 3.png" alt="Post 3">
              <div class="day-number">25</div>
            </div>
            <div class="calendar-day">26</div>
            <div class="calendar-day">27</div>
            <!-- Week 5 -->
            <div class="calendar-day">28</div>
            <div class="calendar-day">29</div>
            <div class="calendar-day">30</div>
            <div class="calendar-day empty"></div>
            <div class="calendar-day empty"></div>
            <div class="calendar-day empty"></div>
            <div class="calendar-day empty"></div>
          </div>"""

# 1. Update HTML
with open('/Users/luxfajah/claudia_mattanna/junho.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace calendar
html = re.sub(r'<div class="calendar-grid">.*?</div>\s*</div>\s*</div>', calendar_html + '\n        </div>\n      </div>', html, flags=re.DOTALL)

# Fix Post 3 path
html = html.replace('Junho/Post 3/Post 3.png', 'Junho/Post 3.png')

with open('/Users/luxfajah/claudia_mattanna/junho.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update JS
with open('/Users/luxfajah/claudia_mattanna/junho.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('Junho/Post 3/Post 3.png', 'Junho/Post 3.png')

with open('/Users/luxfajah/claudia_mattanna/junho.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Calendar and Post 3 path fixed!")
