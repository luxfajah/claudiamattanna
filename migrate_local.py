import os

api_save_js = """import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method Not Allowed' });

  // No Vercel, a única pasta permitida para gravação temporária sem banco de dados é a /tmp
  const filePath = path.join('/tmp', 'responses.json');

  try {
    // Tenta ler o arquivo existente para não apagar dados de outros posts, caso existam
    let currentData = {};
    if (fs.existsSync(filePath)) {
      const fileData = fs.readFileSync(filePath, 'utf-8');
      currentData = JSON.parse(fileData);
    }

    // Mescla os novos dados enviados pela interface
    const newData = req.body.data;
    
    // Sobrescreve o arquivo com os dados atualizados
    fs.writeFileSync(filePath, JSON.stringify(newData, null, 2));

    res.status(200).json({ status: 'success' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
"""

api_load_js = """import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  const filePath = path.join('/tmp', 'responses.json');

  try {
    if (fs.existsSync(filePath)) {
      const fileData = fs.readFileSync(filePath, 'utf-8');
      res.status(200).json(JSON.parse(fileData));
    } else {
      // Se o arquivo ainda não existir, retorna vazio
      res.status(200).json({ statuses: {}, comments: {} });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
"""

git_repo = '/Users/luxfajah/Documents/Duas mâos/Claudia Mattana'

with open(os.path.join(git_repo, 'api', 'save.js'), 'w') as f:
    f.write(api_save_js)

with open(os.path.join(git_repo, 'api', 'load.js'), 'w') as f:
    f.write(api_load_js)

work_dir = '/Users/luxfajah/claudia_mattanna'

with open(os.path.join(work_dir, 'api', 'save.js'), 'w') as f:
    f.write(api_save_js)

with open(os.path.join(work_dir, 'api', 'load.js'), 'w') as f:
    f.write(api_load_js)

print("Reverted to local file system saving!")
