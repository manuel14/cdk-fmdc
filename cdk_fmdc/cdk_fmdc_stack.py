from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda,
    aws_lambda_event_sources as event_sources,
    core,
    
)
from constructs import Construct


class CdkFmdcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkFmdcQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        input_s3_bucket = s3.Bucket(
            self,
            "TestBucket"
        )

        s3_file_split_lambda = aws_lambda.Function(
            self,
            'S3FileSplit',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.asset('lambda_function'),
            handler='s3_file_handling.lambda_handler',
            timeout=core.Duration.minutes(5),
        )
        input_s3_bucket.grant_read_write(s3_file_split_lambda)
        s3_file_split_lambda.add_event_source(
            event_sources.S3EventSource(
                input_s3_bucket,
                events=[s3.EventType.OBJECT_CREATED],
                filters=[]
            )
        )