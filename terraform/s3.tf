resource "aws_s3_bucket" "images" {

  bucket = "image-processing-output-demo-123456"

  tags = local.common_tags
}

resource "aws_s3_bucket_versioning" "versioning" {

  bucket = aws_s3_bucket.images.id

  versioning_configuration {

    status = "Enabled"
  }
}