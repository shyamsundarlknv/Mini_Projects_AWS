import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    try:
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
            'body': json.dumps('Student data saved successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
