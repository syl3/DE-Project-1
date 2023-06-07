## AWS account level config: region
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

## AWS S3 bucket details
variable "bucket_prefix" {
  description = "Bucket prefix for our datalake"
  type        = string
  default     = "sde-data-lake-"
}


## AWS Redshift credentials and node type
variable "redshift_user" {
  description = "AWS user name for Redshift"
  type        = string
  default     = "sde_user"
}

variable "redshift_password" {
  description = "AWS password for Redshift"
  type        = string
  default     = "sdeP0ssword0987"
}

variable "redshift_node_type" {
  description = "AWS Redshift node  type"
  type        = string
  default     = "dc2.large"
}



# Setting as budget monitor, so we don't go over 10 USD per month
resource "aws_budgets_budget" "cost" {
  budget_type  = "COST"
  limit_amount = "10"
  limit_unit   = "USD"
  time_unit    = "MONTHLY"
}