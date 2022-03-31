def lambda_handler(event, context):
    print('Received event: \n' + str(event))
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print("file key is {}".format(key))