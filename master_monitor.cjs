// OMEGA MASTER MONITOR — one converged poll across cash channels (balances + fresh tasks).
// Read-only. Never prints secrets. Income = ONLY settled balances > 0.
process.noDeprecation = true;
const fs = require('fs');
const H = '/home/hatch/workspace/goals/1000-2000/hidden_files';
const now = new Date();

async function j(url, headers) {
  const r = await fetch(url, { headers, signal: AbortSignal.timeout(25000) });
  return r.json();
}

(async () => {
  const out = { at: now.toISOString() };
  // 1) TaskForce: board fresh + earnings
  try {
    const rec = JSON.parse(fs.readFileSync(H + '/taskforce_agent.json', 'utf8'));
    const d = await j('https://www.task-force.app/api/agent/tasks?status=ACTIVE&limit=100', { 'X-API-Key': rec.api_key });
    const tasks = d.tasks || [];
    const stPath = H + '/tf_master_seen.json';
    let seen = {}; try { seen = JSON.parse(fs.readFileSync(stPath, 'utf8')); } catch {}
    const EXEC = /data|research|writing|content|development|coding|testing|analysis|documentation/i;
    const HUMAN = /video|face|record|photo|screenshot|selfie|voice|call|onsite|in-person|device/i;
    const fresh = [];
    for (const t of tasks) {
      if (!t.id) continue;
      if (!seen[t.id]) {
        seen[t.id] = 1;
        const okD = !t.deadline || new Date(t.deadline) > now;
        if (new Date(t.createdAt || 0) > new Date('2026-10-01T00:00:00Z') && okD && Number(t.slotsAvailable || 0) > 0 &&
            EXEC.test(String(t.category) + ' ' + String(t.title) + ' ' + String(t.description)) && !HUMAN.test(String(t.title))) {
          fresh.push({ id: t.id, title: t.title, pay: t.paymentPerWorker, deadline: t.deadline });
        }
      }
    }
    fs.writeFileSync(stPath, JSON.stringify(seen));
    const e = await j('https://www.task-force.app/api/agent/earnings', { 'X-API-Key': rec.api_key });
    out.taskforce = { board: tasks.length, fresh, earnings: e.totalEarnings ?? 0 };
  } catch (e) { out.taskforce = { error: String(e.message || e) }; }
  // 2) Superteam: live listings
  try {
    const rec = JSON.parse(fs.readFileSync(H + '/superteam_agent.json', 'utf8'));
    const d = await j('https://superteam.fun/api/agents/listings/live?take=50', { Authorization: 'Bearer ' + rec.apiKey, 'User-Agent': 'OMEGA-SINGULARITY/1.0' });
    const lst = Array.isArray(d) ? d : (d.listings || d.data || []);
    out.superteam = { live: lst.length, titles: lst.map(l => l.title) };
  } catch (e) { out.superteam = { error: String(e.message || e) }; }
  // 3) TaskBounty: board
  try {
    const d = await j('https://www.task-bounty.com/api/v1/tasks', {});
    out.taskbounty = { tasks: (d.data || []).length };
  } catch (e) { out.taskbounty = { error: String(e.message || e) }; }
  console.log(JSON.stringify(out));
})().catch(e => { console.log(JSON.stringify({ fatal: String(e.message || e) })); process.exit(1); });
