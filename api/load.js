import { createClient } from 'redis';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');

  const client = createClient({ url: process.env.REDIS_URL || process.env.KV_URL || "redis://default:YpxigeuX75iY6FvCubASt2ruLVBKImHF@redis-10083.c92.us-east-1-3.ec2.cloud.redislabs.com:10083" });

  try {
    await client.connect();
    const raw = await client.get('claudia_responses');
    await client.disconnect();
    res.status(200).json(raw ? JSON.parse(raw) : {});
  } catch (e) {
    try { await client.disconnect(); } catch {}
    res.status(500).json({ error: e.message });
  }
}
