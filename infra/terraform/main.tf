# main.tf — AWS provider and basic configurations
provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "housing_mlops_repo" {
  name = "housing-mlops-repo"
}

resource "aws_s3_bucket" "housing_mlops_bucket" {
  bucket = "housing-mlops-bucket"
}

resource "aws_instance" "housing_mlops_ec2" {
  ami = var.ec2_ami
  instance_type = var.ec2_instance_type
  key_name = var.ec2_key_name

  tags = {
    Name = "housing-mlops-ec2-instance"
  }

  # Example security group and user data to run a Docker container (optional)
  security_groups = ["housing-mlops-sg"]
}

resource "aws_security_group" "housing_mlops_sg" {
  name        = "housing-mlops-sg"
  description = "Allow inbound HTTP and SSH traffic"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

