export default async function handler(req, res) {
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
