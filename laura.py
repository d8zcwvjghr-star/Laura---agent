import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("agent.md", "r", encoding="utf-8") as f:
    instructions = f.read()

print("Laura is ready.")
print("Instructions loaded:", len(instructions), "characters")
