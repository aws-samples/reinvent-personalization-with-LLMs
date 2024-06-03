import boto3

# Initialize the Bedrock client
bedrock_client = boto3.client(service_name='bedrock-runtime')
bedrock_agent_client = boto3.client("bedrock-agent-runtime", region_name = 'us-east-1')
accept = "application/json"
contentType = "application/json"