import os
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    # aws_sqs as sqs,
)

import aws_cdk.aws_lambda_python_alpha as lambda_python
from constructs import Construct

class CdkPythonTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        lambda_python.PythonFunction(
            self, "handlingFunction",
            entry=os.path.join(os.path.dirname(
                os.path.realpath(__file__)), "../src/lambda"),
            runtime=_lambda.Runtime.PYTHON_3_9,
            index="lambda_function.py",
            environment={
                "LOGLEVEL": "DEBUG"
            },
            timeout=Duration.seconds(20),
            memory_size=512,
            tracing=_lambda.Tracing.ACTIVE
        )

