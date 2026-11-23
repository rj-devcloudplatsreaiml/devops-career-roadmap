# Lab 08: Ansible Configuration Management

Demonstrates idempotent configuration automation using an inventory and playbook (`playbooks/baseline.yml`), validated in CI with syntax checks and a dry-run check pass.

## Structure

- `inventory/hosts.ini` — Target host inventory (`app_nodes`)
- `playbooks/baseline.yml` — Idempotent directory and status file configuration tasks
- `.github/workflows/lab-08-ci.yml` — Runs `ansible-playbook --syntax-check` and `--check` mode on push/PR
