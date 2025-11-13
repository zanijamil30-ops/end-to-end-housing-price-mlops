# variables.tf — Terraform variables for easy configuration

variable "aws_region" {
  description = "AWS Region"
  default     = "us-east-1"
}

variable "ec2_ami" {
  description = "AMI ID for EC2 instance"
  default     = "ami-12345678"  # Replace with a valid AMI ID
}

variable "ec2_instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ec2_key_name" {
  description = "EC2 SSH Key Name"
  default     = "your-ssh-key"  # Replace with your SSH key name
}
