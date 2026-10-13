// OMEGA TaskForce specialist — polls live board via official agent API.
// Flags genuinely fresh, funded, executable tasks. NEVER applies autonomously per task without standing rules.
// Key lives ONLY in hidden taskforce_agent.json (mode 600) — never printed.
const fs = require('fs');

const STATE_FILE = process.env.STATE_FILE;
const KEYFILE = process.env.KEYFILE;
const now = new Date();

function loadState() { try { return JSON.parse(fs.readFileSync(STATE_FILE, 'utf8')); } catch { return { seen: {} }; } }
function saveState(s) { fs.writeFileSync(STATE_FILE, JSON.stringify(s, null, 2)); }

const EXECUTIVE = /data|research|writing|content|development|coding|testing|analysis|documentation/i;
const HUMAN_ONLY = /video|face|record|photo|screenshot|selfie|voice|call|onsite|in-person|device/i;

(async () => {
  const rec = JSON.parse(fs.readFileSync(KEYFILE, 'utf8'));
  const r = await fetch('https://www.task-force.app/api/agent/tasks?status=ACTIVE&limit=100', { headers: { 'X-API-Key': rec.api_key } });
  const d = await r.json();
  const tasks = d.tasks || [];
  const state = loadState();
  const fresh = [];
  for (const t of tasks) {
    if (!t.id) continue;
    if (!state.seen[t.id]) {
      state.seen[t.id] = { firstSeen: now.toISOString(), title: t.title };
      const created = new Date(t.createdAt || 0);
      const deadline = t.deadline ? new Date(t.deadline) : null;
      const freshCreated = created > new Date('2026-10-01T00:00:00Z');
      const okDeadline = !deadline || deadline > now;
      const slots = Number(t.slotsAvailable || 0) > 0;
      const title = String(t.title || ''), cat = String(t.category || '');
      const executable = EXECUTIVE.test(cat + ' ' + title + ' ' + String(t.description || '')) && !HUMAN_ONLY.test(title);
      if (freshCreated && okDeadline && slots && executable) {
        fresh.push({ id: t.id, title, pay: t.paymentPerWorker, total: t.totalBudget, category: cat, deadline: t.deadline, slots: t.slotsAvailable });
      }
    }
  }
  saveState(state);
  console.log(JSON.stringify({ at: now.toISOString(), board: tasks.length, freshCandidates: fresh }));
})().catch(e => { console.log(JSON.stringify({ error: String(e.message || e) })); process.exit(1); });
