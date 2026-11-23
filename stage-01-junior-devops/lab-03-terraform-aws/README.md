# Lab 03: Terraform AWS Infrastructure & CI

Declarative Infrastructure as Code (IaC) defining a hardened AWS S3 artifact bucket with versioning, AES-256 encryption, and strict public access blocking, validated automatically via GitHub Actions.

## Architecture & Files

- `versions.tf` — Terraform CLI and AWS provider constraints
- `variables.tf` — Input variables (`aws_region`, `project_name`, `environment`)
- `main.tf` — S3 bucket, versioning, encryption, and public access block resources
- `outputs.tf` — Bucket ID and ARN outputs
- `.github/workflows/ci.yml` — Automated formatting (`fmt`), initialization (`init`), and validation (`validate`) pipeline

## Usage

Initialize and validate locally:
`terraform init -backend=false`
`terraform fmt -check`
`terraform validate`

Plan and apply (requires AWS credentials):
`terraform plan`
`terraform apply`
