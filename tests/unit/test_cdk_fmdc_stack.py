import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_fmdc.cdk_fmdc_stack import CdkFmdcStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_fmdc/cdk_fmdc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkFmdcStack(app, "cdk-fmdc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
