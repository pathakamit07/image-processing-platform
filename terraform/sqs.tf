resource "aws_sqs_queue" "dlq" {

  name = "${var.project_name}-dlq"

  message_retention_seconds = 1209600

  tags = local.common_tags
}

resource "aws_sqs_queue" "main" {

  name = "${var.project_name}-queue"

  visibility_timeout_seconds = 300

  receive_wait_time_seconds = 20

  message_retention_seconds = 1209600

  redrive_policy = jsonencode({

    deadLetterTargetArn = aws_sqs_queue.dlq.arn

    maxReceiveCount = 5
  })

  tags = local.common_tags
}