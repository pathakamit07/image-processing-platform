variable "aws_region" {

  type = string

  default = "us-east-1"
}

variable "project_name" {

  type = string

  default = "image-processing"
}

variable "environment" {

  type = string

  default = "dev"
}

variable "cluster_version" {

  type = string

  default = "1.30"
}