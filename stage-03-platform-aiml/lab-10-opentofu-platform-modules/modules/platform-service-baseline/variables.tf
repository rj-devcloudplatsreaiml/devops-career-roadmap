variable "service_name" {
  description = "Name of the internal platform or ML service"
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9-]+$", var.service_name))
    error_message = "service_name must use lowercase letters, numbers, and hyphens only."
  }
}

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be one of: dev, staging, prod."
  }
}

variable "cost_center" {
  description = "FinOps cost allocation tag"
  type        = string
}

variable "enable_versioning" {
  description = "Enable S3 artifact versioning for rollback safety"
  type        = bool
  default     = true
}
