import re
import os

new_login_js = """export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method Not Allowed' });

  const { username, password } = req.body;

  const validUsers = {
    // Admin variations
    'admin@duasmaos.com.br': 'T7v#S26!Adm9Xp',
    'admin': 'T7v#S26!Adm9Xp',
    
    // Client variations (Claudia Mattanna)
    'claudia@duasmaos.com.br': 'claudia2026',
    'claudia': 'claudia2026'
  };

  const userLower = username?.toLowerCase().trim();
  if (validUsers[userLower] && validUsers[userLower] === password) {
    return res.status(200).json({ success: true, username: userLower, token: `token_valid_${userLower.replace(/[^a-z0-9]/g, '')}` });
  }

  return res.status(401).json({ success: false, error: 'Usuário ou senha incorretos' });
}
"""

paths = [
    '/Users/luxfajah/claudia_mattanna/api/login.js',
    '/Users/luxfajah/Documents/Duas mâos/Claudia Mattana/api/login.js'
]

for path in paths:
    if os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_login_js)

print("Credentials updated!")
