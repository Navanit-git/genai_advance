from pydantic import BaseModel
from openai import OpenAI
import json
with open("../keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_key_1
)

# Example of structured output parsing with OpenAI's Groq API
# class CalendarEvent(BaseModel):
#     name: str
#     date: str
#     participants: list[str]

# completion = client.beta.chat.completions.parse(
#     model="meta-llama/llama-4-scout-17b-16e-instruct",
#     messages=[
#         {"role": "system", "content": "Extract the event information."},
#         {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
#     ],
#     response_format=CalendarEvent,
# )
# print(completion)
# print(completion.choices[0].message.content)
# {
#   "name": "science fair",
#   "date": "Friday",
#   "participants": ["Alice", "Bob"]
# }





# class Step(BaseModel):
#     explanation: str
#     output: str

# class MathReasoning(BaseModel):
#     steps: list[Step]
#     final_answer: str

# completion = client.beta.chat.completions.parse(
#     model="meta-llama/llama-4-scout-17b-16e-instruct",
#     messages=[
#         {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
#         {"role": "user", "content": "how can I solve 8x + 7 = -23"}
#     ],
#     response_format=MathReasoning,
# )

# print(completion)
# ParsedChatCompletion[MathReasoning](id='chatcmpl-8661aaf6-264f-4e1a-a917-858c72bde7a3', choices=[ParsedChoice[MathReasoning](finish_reason='stop', index=0, logprobs=None, message=ParsedChatCompletionMessage[MathReasoning](content='{\n  "steps": [\n    {\n      "explanation": "To isolate the term with x, we need to get rid of the constant term on the same side. We can do this by subtracting 7 from both sides of the equation.",\n      "output": "8x + 7 - 7 = -23 - 7"\n    },\n    {\n      "explanation": "Simplifying both sides gives us:",\n      "output": "8x = -30"\n    },\n    {\n      "explanation": "Now, to solve for x, we need to get rid of the coefficient of x, which is 8. We can do this by dividing both sides by 8.",\n      "output": "8x / 8 = -30 / 8"\n    },\n    {\n      "explanation": "Simplifying both sides gives us:",\n      "output": "x = -30/8"\n    },\n    {\n      "explanation": "We can simplify the fraction on the right side.",\n      "output": "x = -15/4"\n    }\n  ],\n  "final_answer": "x = -15/4 or x = -3.75"\n}', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=MathReasoning(steps=[Step(explanation='To isolate the term with x, we need to get rid of the constant term on the same side. We can do this by subtracting 7 from both sides of the equation.', output='8x + 7 - 7 = -23 - 7'), Step(explanation='Simplifying both sides gives us:', output='8x = -30'), Step(explanation='Now, to solve for x, we need to get rid of the coefficient of x, which is 8. We can do this by dividing both sides by 8.', output='8x / 8 = -30 / 8'), Step(explanation='Simplifying both sides gives us:', output='x = -30/8'), Step(explanation='We can simplify the fraction on the right side.', output='x = -15/4')], final_answer='x = -15/4 or x = -3.75')))], created=1754569668, model='meta-llama/llama-4-scout-17b-16e-instruct', object='chat.completion', service_tier='on_demand', system_fingerprint='fp_79da0e0073', usage=CompletionUsage(completion_tokens=245, prompt_tokens=195, total_tokens=440, completion_tokens_details=None, prompt_tokens_details=None, queue_time=0.122886154, prompt_time=0.011192876, completion_time=0.633439341, total_time=0.644632217), usage_breakdown=None, x_groq={'id': 'req_01k2280xbvf0vv5awfexvk4kfn'})
# print(completion.choices[0].message.content)

# {
#   "steps": [
#     {
#       "explanation": "To isolate the term with x, we need to get rid of the constant term on the same side. We can do this by subtracting 7 from both sides of the equation.",
#       "output": "8x + 7 - 7 = -23 - 7"
#     },
#     {
#       "explanation": "Simplifying both sides gives us:",
#       "output": "8x = -30"
#     },
#     {
#       "explanation": "Now, to solve for x, we need to get rid of the coefficient of x, which is 8. We can do this by dividing both sides by 8.",
#       "output": "8x / 8 = -30 / 8"
#     },
#     {
#       "explanation": "Simplifying both sides gives us:",
#       "output": "x = -30/8"
#     },
#     {
#       "explanation": "We can simplify the fraction on the right side.",
#       "output": "x = -15/4"
#     }
#   ],
#   "final_answer": "x = -15/4 or x = -3.75"
# }


from enum import Enum
from typing import Optional

class Category(str, Enum):
    violence = "violence"
    sexual = "sexual"
    self_harm = "self_harm"

class ContentCompliance(BaseModel):
    is_violating: bool
    category: Optional[Category]
    explanation_if_violating: Optional[str]

completion = client.beta.chat.completions.parse(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {"role": "system", "content": "Determine if the user input violates specific guidelines and explain if they do."},
        {"role": "user", "content": "How do I fight unecessarily?"}
    ],
    response_format=ContentCompliance,
)

print(completion.choices[0].message.content)






# 'message': 'This model does not support response format `json_schema`. Please use a different model or remove the response format.'}
# This error indicates that the model you are using does not support the specified response format.
# You may need to choose a different model that supports structured output or adjust your request accordingly.


# JSON is JavaScript Object Notation