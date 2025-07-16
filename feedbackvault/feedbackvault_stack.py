from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as ddb,
    RemovalPolicy,
    Duration
)
from constructs import Construct

class FeedbackvaultStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB Table
        table = ddb.Table(
            self, "FeedbackTable",
            partition_key={"name": "email", "type": ddb.AttributeType.STRING},
	    removal_policy=RemovalPolicy.DESTROY

        )

        # Lambda Function
        handler = _lambda.Function(
            self, "FeedbackHandler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="feedback_handler.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": table.table_name
            },
            timeout=Duration.seconds(10)
        )

        # Grant Lambda access to DynamoDB
        table.grant_read_write_data(handler)

        # API Gateway
        api = apigw.LambdaRestApi(
            self, "FeedbackAPI",
            handler=handler,
            proxy=True
        )
