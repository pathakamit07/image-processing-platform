resource "aws_iam_policy" "worker_policy" {

  name = "${var.project_name}-worker-policy"

  policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Action = [

          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:ChangeMessageVisibility",
          "sqs:GetQueueAttributes"
        ]

        Resource = "*"
      },

      {

        Effect = "Allow"

        Action = [

          "s3:PutObject",
          "s3:GetObject",
          "s3:HeadObject"
        ]

        Resource = "*"
      },

      {

        Effect = "Allow"

        Action = [

          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:DeleteItem"
        ]

        Resource = "*"
      },

      {

        Effect = "Allow"

        Action = [

          "cloudwatch:PutMetricData"
        ]

        Resource = "*"
      }
    ]
  })
}