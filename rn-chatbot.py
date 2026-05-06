import time

import json

from groq import Groq

import os

from dotenv import load_dotenv

load_dotenv("rn.env")

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

if os.path.exists("memory.json"):
    with open("memory.json","r") as f:
        messages = json.load(f)
else:
    messages = [{"role": "system", "content": "you are my homie RN if i,m wrong then correct where i make mistake correct me make me understand make me sharper and learn from my mistake..."}]

for char in "=" * 30:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
for char in "     RN is online ":
    print(char, end="", flush=True)
    time.sleep(0.05)
print()
for char in "=" * 30:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
print()
while True:
    question = input("ASSISTANT RN (type 'quit' to stop): ")
    if question == "quit":
        break

    messages.append({"role": "user", "content": question})

    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(reply)
    with open ("memory.json","w") as f:
        json.dump(messages,f)

       