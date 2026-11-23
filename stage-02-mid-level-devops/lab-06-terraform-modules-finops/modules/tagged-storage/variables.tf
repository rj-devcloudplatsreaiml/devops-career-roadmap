variable "bucket_name" {
  type        = string
  description = "Globally unique S3 bucket name"
}

variable "environment" {
  type        = string
  description = "Environment identifier (e.g., dev, prod)"
}

variable "cost_center" {
  type        = string
  description = "FinOps cost center tag for billing attribution"
}

variable "owner" {
  type        = string
  description = "Owning team or service tag"
}

variable "noncurrent_expiration_days" {
  type        = number
  default     = 30
  description = "Days before noncurrent object versions expire to control storage costs"
}
