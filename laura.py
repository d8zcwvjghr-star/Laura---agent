import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("agent.md", "r", encoding="utf-8") as f:
    instructions = f.read()

response = client.responses.create(
    model="gpt-5-mini",
    instructions=instructions,
    input="Hello Laura. Introduce yourself and tell me what you can help me with."
)

print(response.output_text)
