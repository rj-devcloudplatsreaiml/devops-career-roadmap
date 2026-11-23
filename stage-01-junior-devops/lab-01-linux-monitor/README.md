# Linux Health & Log Monitor (Junior DevOps Lab 01)

A lightweight Bash health-check utility with automated smoke tests and GitHub Actions CI.

## Project Structure

- `.github/workflows/ci.yml` — Automated CI checks on push/PR
- `logs/` — Runtime logs (ignored by Git)
- `scripts/health_check.sh` — Main disk & memory check script
- `scripts/test_health_check.sh` — Automated test runner
- `.gitignore` — Excludes runtime logs and OS files

## Usage

Run the health check with a custom disk threshold percentage (default is `85`):

    ./scripts/health_check.sh 80

Run the test suite:

    ./scripts/test_health_check.sh
