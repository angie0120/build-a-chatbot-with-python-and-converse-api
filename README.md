# Build a Simple Chatbot with Amazon Bedrock’s Converse API + Python

---

## About this project

This project is a simple terminal-based chatbot built with Python, boto3, and Amazon Bedrock’s Converse API. It allows you to type messages in your terminal, get responses from a Bedrock foundation model, and continue chatting until you type `exit`.

---

## Why this project is important

If you’re learning Amazon Bedrock, it’s easy to stop at “one prompt → one response.”

This project is important because it demonstrates the next real step:
✅ Building an actual conversation loop by storing message history and sending it back to the model each time.

It shows the core concept behind real chat apps:

user sends message

assistant responds

conversation history is preserved

the model responds with context

---

## Logic Flow



---

## Quick Start

1) AWS Credentials

Configure your AWS credentials using:
```bash 
aws configure sso
# or 
aws configure
```

To confirm you're authenticated:

`aws sts get-caller-identity`

2) Create a virtual environment (recommended)

`python3 -m venv venv`

Activate it:
`source venv/bin/activate`        # macOS/Linux
`venv\Scripts\activate`           # Windows


3) Install boto3
`pip install boto3`

### Run the script
python chatbot.py


You should see:

`Bedrock Chatbot is running! Type 'exit' to quit.`

---

## Code explanation


