import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "amazon.nova-micro-v1:0"

print("Bedrock Chatbot is running! Type 'exit' to quit.\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Bye!")
        break

    messages.append(
        {
            "role": "user",
            "content": [{"text": user_input}],
        }
    )

    response = client.converse(
        modelId=model_id,
        messages=messages,
        inferenceConfig={"maxTokens": 100, "temperature": 0.7},
    )

    bot_reply = response["output"]["message"]["content"][0]["text"]

    print(f"Chatbot: {bot_reply}\n")

    messages.append(
        {
            "role": "assistant",
            "content": [{"text": bot_reply}],
        }
    )
