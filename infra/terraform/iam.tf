# iam.tf — IAM role and policies for EC2

resource "aws_iam_role" "housing_mlops_ec2_role" {
  name = "housing-mlops-ec2-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy" "housing_mlops_ec2_policy" {
  name = "housing-mlops-ec2-policy"
  role = aws_iam_role.housing_mlops_ec2_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:*",
          "ecr:*"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

