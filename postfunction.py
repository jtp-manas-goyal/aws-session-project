import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SecretMessages')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        target_name = body.get('targetName', '').lower()
        message = body.get('message', '')
        timestamp = int(time.time() * 1000)

        item = {
            'targetName': target_name,
            'timestamp': timestamp,
            'message': message
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({ 'status': 'Message stored secretly' })
        }


    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({ 'error': 'Failed to store message', 'detail': str(e) })
        }

