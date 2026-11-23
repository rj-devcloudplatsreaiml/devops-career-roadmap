terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

module "app_artifacts" {
  source                     = "../../modules/tagged-storage"
  bucket_name                = "rj-prod-app-artifacts-2026"
  environment                = "prod"
  cost_center                = "platform-core"
  owner                      = "devops-team"
  noncurrent_expiration_days = 90
}
