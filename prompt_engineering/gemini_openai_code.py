# Ref = https://ai.google.dev/gemini-api/docs/openai
# rate limit = https://ai.google.dev/gemini-api/docs/rate-limits
# ai studio = https://aistudio.google.com/app/apikey
# cloud console = https://console.cloud.google.com/apis/dashboard

import json 

with open("keys.json") as f:
    api_key = json.load(f)


gemini_key_1 =api_key["google_api_key_1"]
gemini_key_2 =api_key["google_api_key_2"]
gemini_key_3 =api_key["google_api_key_3"]



from openai import OpenAI

client = OpenAI(
  api_key=gemini_key_2,
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# ## list models
# models = client.models.list()
# for model in models:
#   print(model.id)


#simple chat completion
# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Explain to me how AI works"
#         }
#     ]
# )

# print(response.choices[0].message)


# # # reasoning
# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     # reasoning_effort="low",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "how many r's are in the word strawberry"
#         }
#     ],
#     extra_body={
#       'extra_body': {
#         "google": {
#           "thinking_config": {
#             "thinking_budget": 800,
#             "include_thoughts": True
#           }
#         }
#       }
#     }
# )
# print(response)
# print(response.choices[0].message)





#structured output 

# from pydantic import BaseModel
# from openai import OpenAI


# class CalendarEvent(BaseModel):
#     name: str
#     date: str
#     participants: list[str]

# completion = client.beta.chat.completions.parse(
#     model="gemini-2.0-flash",
#     messages=[
#         {"role": "system", "content": "Extract the event information."},
#         {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
#     ],
#     response_format=CalendarEvent,
# )

# print(completion.choices[0].message.parsed)


from google import genai
from google.genai import types

client = genai.Client(api_key=gemini_key_1)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)


