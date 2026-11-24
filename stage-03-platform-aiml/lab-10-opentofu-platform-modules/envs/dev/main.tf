provider "aws" {
  region                      = "ap-south-1"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
}

module "ml_inference_baseline" {
  source = "../../modules/platform-service-baseline"

  service_name      = "fraud-scoring-api"
  environment       = "dev"
  cost_center       = "CC-AIML-402"
  enable_versioning = true
}

output "dev_bucket" {
  value = module.ml_inference_baseline.artifact_bucket_name
}

output "dev_tags" {
  value = module.ml_inference_baseline.applied_finops_tags
}
