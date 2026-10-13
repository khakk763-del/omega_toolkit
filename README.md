# OMEGA Toolkit

Personal automation utilities behind the OMEGA studio's daily operations: channel monitors and campaign helpers. Read-only by design — nothing here moves money or sends anything on its own.

## Scripts

| Script | What it does |
|---|---|
| `master_monitor.cjs` | One converged poll across income channels (balances + fresh tasks). Read-only; never prints secrets |
| `taskforce_watcher.cjs` | Watches a freelance task board for fresh matching tasks |
| `zaph_watcher.cjs` | Watches a second task marketplace for new postings |
| `send_campaign.py` | Authorized Instagram DM campaign sender (12 personalized DMs, paced) with send logging |

## Notes

- Credentials live outside the repo (never committed) — the monitors read them from a local secrets dir at runtime.
- These are operator tools, not a framework: adapt the selectors and endpoints before reuse.

Built by **OMEGA Studio**.
