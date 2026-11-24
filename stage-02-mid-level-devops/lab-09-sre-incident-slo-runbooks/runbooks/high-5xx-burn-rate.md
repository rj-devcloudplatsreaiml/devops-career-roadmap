# Runbook: CheckoutHighErrorBudgetBurnFast

## 1. Triage (First 2 Minutes)
1. Check ArgoCD sync status and latest deployment diff (`argocd app get checkout-api`).
2. Inspect pod health and recent restarts (`kubectl get pods -n checkout -l app=checkout-api`).
3. Filter 5xx logs for top upstream dependency errors (`kubectl logs -n checkout -l app=checkout-api --since=10m | grep -E "50[0-4]"`).

## 2. Immediate Mitigation (Target MTTR < 8 Minutes)
- **If caused by a recent release:** Roll back via GitOps (`git revert` on the manifest repo or `argocd app rollback checkout-api`).
- **If caused by traffic spike / saturation:** Scale replicas (`kubectl scale deploy/checkout-api -n checkout --replicas=6`) and verify HPA ceiling.
- **If caused by downstream DB/payment timeout:** Enable circuit-breaker / degraded checkout flag.

## 3. Verification & Follow-Up
- Confirm 5xx burn rate drops below `1.0x` for 10 consecutive minutes.
- Open a blameless postmortem using `runbooks/postmortem-template.md` if > 10% of the 30d error budget was burned.
