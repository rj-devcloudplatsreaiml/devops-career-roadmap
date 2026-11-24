# Blameless Postmortem: [Incident Title]

- **Date / Duration:** YYYY-MM-DD | HH:MM–HH:MM UTC (Total: XX mins)
- **Severity / Impact:** SEV-2 | XX% of checkout requests affected; XX% of 30d error budget consumed
- **MTTR Breakdown:** Detect (Xm) -> Triage (Xm) -> Mitigate (Xm)

## What Happened
Concise summary of user impact and root trigger.

## Timeline (UTC)
- `HH:MM` — Alert `CheckoutHighErrorBudgetBurnFast` fired.
- `HH:MM` — On-call identified bad config/deployment via ArgoCD history.
- `HH:MM` — Rollback completed; 5xx rate returned to baseline.

## Action Items
- [ ] Add pre-merge Checkov/OPA policy or canary gate to catch regression before rollout.
- [ ] Update runbook with exact dashboard query used during triage.
