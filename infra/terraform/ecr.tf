# ecr.tf — AWS Elastic Container Registry (ECR) setup

resource "aws_ecr_repository" "housing_mlops_repo" {
  name = "housing-mlops-repository"
  image_tag_mutability = "MUTABLE"
}

