import json
with open("../keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]


from llama_index.llms.groq import Groq
llm = Groq(model="llama3-70b-8192", api_key=groq_key_1)
# response = llm.complete("Explain the importance of low latency LLMs")
# print(response)

from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="What is your name"),
]
resp = llm.chat(messages)
print(resp)