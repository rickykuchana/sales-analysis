import boto3
import json

# Create a Bedrock runtime client (boto3's connection to the Bedrock service)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# The model you invoked in the Workbench
model_id = "google.gemma-3-4b-it"

# Build the request body (the prompt, formatted the way Bedrock expects)
body = {
    "messages": [
        {"role": "user", "content": "what is an api in two sentences"}
    ],
    "max_tokens": 300,
}

# Call the model
response = client.invoke_model(
    modelId=model_id,
    body=json.dumps(body),
)

# Read and print the response
result = json.loads(response["body"].read())
# Pull out just the model's text response
answer = result["choices"][0]["message"]["content"]
print("Model response:")
print(answer)

# And the token usage, like your Anthropic script
usage = result["usage"]
print(f"\nTokens - input: {usage['prompt_tokens']}, output: {usage['completion_tokens']}")