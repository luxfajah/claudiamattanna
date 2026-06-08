import json
import os

base_responses = {
  "statuses": {
    "1": "none",
    "2": "none",
    "3": "none"
  },
  "comments": {
    "1": [],
    "2": [],
    "3": []
  }
}

api_save_js = """export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method Not Allowed' });

  const REPO = 'luxfajah/claudiamattanna';
  const FILE_PATH = 'responses.json';
  const TOKEN = process.env.GITHUB_TOKEN;

  if (!TOKEN) return res.status(500).json({ error: 'GITHUB_TOKEN is missing in Vercel settings' });

  try {
    // 1. Get the current file SHA
    const getRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}?t=${Date.now()}`, {
      headers: { 'Authorization': `token ${TOKEN}`, 'Accept': 'application/vnd.github.v3+json' }
    });
    
    if (!getRes.ok) throw new Error('Failed to fetch file SHA from GitHub');
    const getJson = await getRes.json();
    const sha = getJson.sha;

    // 2. Prepare the new content base64 encoded
    const contentBuffer = Buffer.from(JSON.stringify(req.body, null, 2));
    const contentBase64 = contentBuffer.toString('base64');

    // 3. Update the file in the repository
    const putRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}`, {
      method: 'PUT',
      headers: { 'Authorization': `token ${TOKEN}`, 'Accept': 'application/vnd.github.v3+json', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: 'Automated DB update: responses saved',
        content: contentBase64,
        sha: sha
      })
    });

    if (!putRes.ok) throw new Error('Failed to commit to GitHub');
    
    res.status(200).json({ status: 'success' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
"""

api_load_js = """export default async function handler(req, res) {
  const REPO = 'luxfajah/claudiamattanna';
  const FILE_PATH = 'responses.json';
  const TOKEN = process.env.GITHUB_TOKEN;

  try {
    const headers = { 'Accept': 'application/vnd.github.v3+json' };
    if (TOKEN) headers['Authorization'] = `token ${TOKEN}`;
    
    const getRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}?t=${Date.now()}`, { headers });
    
    if (getRes.ok) {
      const getJson = await getRes.json();
      const content = Buffer.from(getJson.content, 'base64').toString('utf-8');
      res.status(200).json(JSON.parse(content));
    } else {
      res.status(200).json({});
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
"""

package_json = """{
  "name": "claudiamattanna",
  "version": "1.0.0",
  "private": true,
  "dependencies": {}
}
"""

# Apply to git repository
git_repo = '/Users/luxfajah/Documents/Duas mâos/Claudia Mattana'

with open(os.path.join(git_repo, 'responses.json'), 'w') as f:
    json.dump(base_responses, f, indent=2)

with open(os.path.join(git_repo, 'api', 'save.js'), 'w') as f:
    f.write(api_save_js)

with open(os.path.join(git_repo, 'api', 'load.js'), 'w') as f:
    f.write(api_load_js)

with open(os.path.join(git_repo, 'package.json'), 'w') as f:
    f.write(package_json)

# Apply to working dir to keep it synced
work_dir = '/Users/luxfajah/claudia_mattanna'
with open(os.path.join(work_dir, 'responses.json'), 'w') as f:
    json.dump(base_responses, f, indent=2)
with open(os.path.join(work_dir, 'api', 'save.js'), 'w') as f:
    f.write(api_save_js)
with open(os.path.join(work_dir, 'api', 'load.js'), 'w') as f:
    f.write(api_load_js)
with open(os.path.join(work_dir, 'package.json'), 'w') as f:
    f.write(package_json)

print("Converted to GitHub API successfully!")
