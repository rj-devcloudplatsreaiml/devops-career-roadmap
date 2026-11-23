variable "aws_region" {
  description = "AWS region for deploying resources"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project prefix used for naming and tagging"
  type        = string
  default     = "devops-junior-lab-03"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}
