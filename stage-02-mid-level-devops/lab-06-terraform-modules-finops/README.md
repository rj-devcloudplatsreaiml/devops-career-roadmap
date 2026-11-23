# Lab 06: Reusable Terraform Modules & FinOps Lifecycle Policies

Demonstrates modular Terraform design across `dev` and `prod` environments using a shared `tagged-storage` module with mandatory FinOps cost-allocation tags, encryption, public access blocks, and lifecycle expiration for noncurrent versions.

## Structure

- `modules/tagged-storage/` — Reusable S3 storage module with versioning, SSE, public access block, and lifecycle rules
- `envs/dev/` — Development environment configuration with shorter noncurrent retention (14 days)
- `envs/prod/` — Production environment configuration with longer noncurrent retention (90 days)
