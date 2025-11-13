# s3.tf — S3 Bucket for storing data/models

resource "aws_s3_bucket" "housing_mlops_bucket" {
  bucket = "housing-mlops-bucket"
  acl    = "private"

  tags = {
    Name        = "housing-mlops-data"
    Environment = "Production"
  }
}

