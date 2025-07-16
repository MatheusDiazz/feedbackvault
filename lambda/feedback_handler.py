import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
	method = event['httpMethod']
	
	if method == 'POST':
		data = json.loads(event['body'])
		table.put_item(Item={'email': data['email'], 'message': data['message']})
		return {'statusCode': 200, 'body': json.dumps({'message': 'Feedback received'})}

	elif method == 'GET':
		response = table.scan()
		return {'statusCode': 200, 'body': json.dumps(response['Items'])}

	return {'statusCode': 405, 'body': json.dumps({'error': 'Method not allowed'})} 
