terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

locals {
  bucket_name = "${var.service_name}-${var.environment}-artifacts"
  common_tags = {
    Service     = var.service_name
    Environment = var.environment
    CostCenter  = var.cost_center
    ManagedBy   = "OpenTofu"
  }
}

resource "aws_s3_bucket" "service_artifacts" {
  bucket = local.bucket_name
  tags   = local.common_tags
}

resource "aws_s3_bucket_public_access_block" "service_artifacts" {
  bucket = aws_s3_bucket.service_artifacts.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "service_artifacts" {
  bucket = aws_s3_bucket.service_artifacts.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "service_artifacts" {
  bucket = aws_s3_bucket.service_artifacts.id

  versioning_configuration {
    status = var.enable_versioning ? "Enabled" : "Suspended"
  }
}
