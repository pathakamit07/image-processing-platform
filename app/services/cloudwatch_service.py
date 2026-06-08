import boto3

from app.config import settings


cloudwatch = boto3.client(
    "cloudwatch",
    region_name=settings.AWS_REGION
)


class CloudWatchService:

    def put_metric(
        self,
        metric_name,
        value
    ):

        cloudwatch.put_metric_data(

            Namespace="ImageProcessing",

            MetricData=[

                {

                    "MetricName": metric_name,

                    "Value": value,

                    "Unit": "Count"
                }
            ]
        )


cloudwatch_service = CloudWatchService()