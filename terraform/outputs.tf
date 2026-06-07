output "cluster_name" {

  value = module.eks.cluster_name
}

output "cluster_endpoint" {

  value = module.eks.cluster_endpoint
}

output "ecr_repository_url" {

  value = aws_ecr_repository.repo.repository_url
}

output "sqs_queue_url" {

  value = aws_sqs_queue.main.id
}

output "s3_bucket_name" {

  value = aws_s3_bucket.images.bucket
}