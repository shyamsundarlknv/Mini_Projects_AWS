import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    try:
        # Check if body is present
        if 'body' not in event or event['body'] is None:
            raise ValueError("Request body is missing or empty")
        
        # Extract data from the incoming event
        body = json.loads(event['body'])
        student_id = body['studentid']
        name = body['name']
        student_class = body['class']
        age = body['age']
        
        # Put the item into the DynamoDB table
        table.put_item(
            Item={
                'studentid': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Student data saved successfully'),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'http://vannakammama.s3-website-us-east-1.amazonaws.com',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
