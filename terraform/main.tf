terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
    redshift = {
      source  = "brainly/redshift"
      version = "1.0.2"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = var.aws_region
  profile = "terraform"
}




# Create our S3 bucket (Datalake)
resource "aws_s3_bucket" "sde-data-lake" {
  bucket_prefix = var.bucket_prefix
  force_destroy = true
}

resource "aws_s3_bucket_ownership_controls" "sde-data-lake" {
  bucket = aws_s3_bucket.sde-data-lake.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}
# Turn block all public access to Off
resource "aws_s3_bucket_public_access_block" "sde-data-lake" {
  bucket = aws_s3_bucket.sde-data-lake.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "sde-data-lake-acl" {
  depends_on = [
    aws_s3_bucket_ownership_controls.sde-data-lake,
    aws_s3_bucket_public_access_block.sde-data-lake,
  ]

  bucket = aws_s3_bucket.sde-data-lake.id
  acl    = "public-read-write"
}

