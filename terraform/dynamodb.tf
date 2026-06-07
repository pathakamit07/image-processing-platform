resource "aws_dynamodb_table" "locks" {

  name = "job-locks"

  billing_mode = "PAY_PER_REQUEST"

  hash_key = "jobId"

  attribute {

    name = "jobId"

    type = "S"
  }

  ttl {

    attribute_name = "ttl"

    enabled = true
  }

  tags = local.common_tags
}

resource "aws_dynamodb_table" "metadata" {

  name = "job-metadata"

  billing_mode = "PAY_PER_REQUEST"

  hash_key = "jobId"

  attribute {

    name = "jobId"

    type = "S"
  }

  tags = local.common_tags
}