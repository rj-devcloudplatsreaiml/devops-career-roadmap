# Lab 07: CI/CD Pipeline Automation & Release Gating

Demonstrates automated release-gate checks in GitHub Actions—verifying script syntax, enforcing semantic version formatting on release metadata, and gating downstream steps on clean checks.

## Structure

- `scripts/check_release_manifest.sh` — Validates service name and `MAJOR.MINOR.PATCH` release version format
- `.github/workflows/lab-07-ci.yml` — Runs shell syntax checks (`bash -n`) and release manifest validation on push/PR
