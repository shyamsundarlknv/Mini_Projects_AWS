import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    try:
        # Scan the DynamoDB table to get all items
        response = table.scan()
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'body': json.dumps(items),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
