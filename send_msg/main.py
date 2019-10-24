import json
import boto3

# ec2Client = boto3.client('ec2')
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-2.amazonaws.com/793267097648/test-dl-queue'

# Try to send a message to sqs queue and returns message id
def send_message(msg):
    return sqs.send_message(
                    QueueUrl=queue_url,
                    DelaySeconds=10,
                    MessageBody=(msg)
                    ).get('MessageId')


def lambda_handler(event, context):
    # regionsRes = ec2Client.describe_regions()

    params = event['queryStringParameters']

    message = params.get('msg', 'default') if params else 'default'
    messageId = send_message(message)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {'message': message,
            'messageId': messageId
            }
        )
    }