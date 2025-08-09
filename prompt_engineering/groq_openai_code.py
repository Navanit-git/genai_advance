#grq api key https://console.groq.com/keys
#groq doc:https://console.groq.com/docs/text-chat
#groq rate limit: https://console.groq.com/settings/limits

import os
import openai
import json 

with open("keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]



client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_key_1
)

# #Normal chat completion
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         # Set a user message for the assistant to respond to.
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],

#     # The language model which will generate the completion.
#     model="qwen/qwen3-32b"
# )

# # Print the completion returned by the LLM.
# print(chat_completion)

# print(chat_completion.choices[0].message.content)




# structured output


# from pydantic import BaseModel
# from typing import Literal
# import json



# class ProductReview(BaseModel):
#     product_name: str
#     rating: float
#     sentiment: Literal["positive", "negative", "neutral"]
#     key_features: list[str]

# response = client.chat.completions.create(
#     # model="moonshotai/kimi-k2-instruct",
#     model ="meta-llama/llama-4-scout-17b-16e-instruct",
#     messages=[
#         {"role": "system", "content": "Extract product review information from the text."},
#         {
#             "role": "user",
#             "content": "I bought the UltraSound Headphones last week and I'm really impressed! The noise cancellation is amazing and the battery lasts all day. Sound quality is crisp and clear. I'd give it 4.5 out of 5 stars.",
#         },
#     ],
#     response_format={
#         "type": "json_schema",
#         "json_schema": {
#             "name": "product_review",
#             "schema": ProductReview.model_json_schema()
#         }
#     }
# )
# print(response)
# review = ProductReview.model_validate(json.loads(response.choices[0].message.content))
# print(json.dumps(review.model_dump(), indent=2))


# reasoning with streaming

import os

from groq import Groq

client = Groq(
    api_key=groq_key_1,
)
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word strawberry",
        }
    ],
    temperature=0.6,
    # max_completion_tokens=1024,
    top_p=0.95,
    stream=True,
    reasoning_format="raw"
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


# reasoning_format 
# parsed	-->     Separates reasoning into a dedicated field while keeping the response concise.
# raw	    -->     Includes reasoning within think tags in the content.
# hidden	-->     Returns only the final answer.