import fs from 'fs';
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
