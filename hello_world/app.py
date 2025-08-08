import os
import boto3
import json

def get_secret(secret_name):
    region_name = os.environ.get('AWS_REGION', 'us-east-1')
    client = boto3.client('secretsmanager', region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret = response.get('SecretString')
    return json.loads(secret) if secret else None

def lambda_handler(event, context):
    secret_name = os.environ.get('SECRET_NAME', 'your-secret-name')
    client_secret_name = os.environ.get('CLIENT_SECRET_NAME', 'your-client-secret-name')

    user_secret = get_secret(secret_name)
    client_secret = get_secret(client_secret_name)

    username = user_secret.get('username') if user_secret else None
    api_token = user_secret.get('api_token') if user_secret else None
    client_id = client_secret.get('client_id') if client_secret else None
    client_secret_value = client_secret.get('client_secret') if client_secret else None

    # Your logic here
    print(f"Username: {username}, API Token: {api_token}")
    print(f"Client ID: {client_id}, Client Secret: {client_secret_value}")

    return {
        "statusCode": 200,
        "body": f"Username: {username}, API Token: {api_token}, Client ID: {client_id}, Client Secret: {client_secret_value}"
    }