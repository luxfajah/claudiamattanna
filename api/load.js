export default async function handler(req, res) {
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
