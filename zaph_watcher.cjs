// OMEGA Zaph dedicated agent watcher — read-only board polling.
// Detects genuinely fresh, funded, executable tasks. NEVER applies/submits/funds.
// Apply requires standing Khalid approval + fresh per-task gates; income route = Zaph wallet -> Khalid.
const fs = require('fs');
const { ZaphWorkClient } = require('@zaphwork/x402-sdk');

const STATE_FILE = process.env.STATE_FILE;
const KEYFILE = process.env.KEYFILE;
const now = new Date();

function loadState() {
  try { return JSON.parse(fs.readFileSync(STATE_FILE, 'utf8')); } catch { return { seen: {} }; }
}
function saveState(s) { fs.writeFileSync(STATE_FILE, JSON.stringify(s, null, 2)); }

const EXEC_CATS = /data|content|writing|seo|development|research|documentation/i;
const HUMAN_ONLY = /screenshot|mobile app|ios|android|video|podcast|audio|logo|design|social media|twitter|instagram|influencer|photo|record/i;

(async () => {
  const rec = JSON.parse(fs.readFileSync(KEYFILE, 'utf8'));
  const client = new ZaphWorkClient({ apiUrl: 'https://zaph.work', privateKey: rec.secretKeyBase58, network: 'mainnet-beta' });
  await client.authenticate();
  const { tasks } = await client.listTasks({ limit: 100 });
  const state = loadState();
  let fresh = [];
  for (const t of tasks || []) {
    const id = t.id;
    if (!id) continue;
    if (!state.seen[id]) {
      state.seen[id] = { firstSeen: now.toISOString(), title: t.title, status: t.status };
      const created = new Date(t.createdAt || 0);
      const deadline = new Date(t.deadline || 0);
      const funded = Number(t.totalFunded || 0) > 0;
      const futureDeadline = deadline > now;
      const freshCreated = created > new Date('2026-10-01T00:00:00Z');
      const title = String(t.title || '');
      const cat = String(t.category || '');
      const executable = EXEC_CATS.test(cat + ' ' + title) && !HUMAN_ONLY.test(title);
      if (t.status === 'open' && funded && futureDeadline && freshCreated && executable) {
        fresh.push({ id, title, pay: t.payment_amount || t.paymentPerWorker || t.budget, currency: t.currency, category: cat, deadline: t.deadline, funded: t.totalFunded, slug: t.slug });
      }
    }
  }
  saveState(state);
  const bal = await client.getBalance().catch(() => null);
  console.log(JSON.stringify({ at: now.toISOString(), board: (tasks || []).length, freshCandidates: fresh, balance: bal }));
})().catch(e => { console.log(JSON.stringify({ error: String(e.message || e) })); process.exit(1); });
