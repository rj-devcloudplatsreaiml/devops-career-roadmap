# Lab 10: OpenTofu Self-Service Platform Modules & Guardrails

## Objective
Build a reusable **OpenTofu** module (`platform-service-baseline`) that enforces:
- Input validation rules (`service_name` regex and allowed `environment` list)
- Mandatory FinOps `CostCenter` tagging
- Secure-by-default S3 storage (public access blocked, AES256 encryption at rest, versioning enabled)
- Offline validation (`tofu fmt`, `tofu validate`, and `checkov`) without requiring cloud credentials
