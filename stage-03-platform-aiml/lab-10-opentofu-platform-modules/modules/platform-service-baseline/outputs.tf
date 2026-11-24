output "artifact_bucket_name" {
  description = "Provisioned artifact/model storage bucket name"
  value       = aws_s3_bucket.service_artifacts.bucket
}

output "applied_finops_tags" {
  description = "Standardized FinOps and ownership tags applied to resources"
  value       = local.common_tags
}
