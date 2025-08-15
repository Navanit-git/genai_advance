import json
import pathlib
api_key_path = pathlib.Path(__file__).parent.parent / "keys.json"
with open(api_key_path) as f:
    api_key = json.load(f)

groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]

import os
from groq import Groq
client = Groq(
    api_key=groq_key_1,
)

from pydantic import BaseModel, Field
from typing import Dict
import json
import re


def extract_and_validate_json(completion, schema_model: BaseModel):
    """
    Extracts JSON from an LLM response, cleans it, and validates against a Pydantic schema.
    """
    raw_output = completion.choices[0].message.content

    # Step 1: Extract JSON block from the response
    json_match = re.search(r"\{[\s\S]*\}", raw_output)
    if not json_match:
        raise ValueError("No JSON object found in the LLM output.")
    json_str = json_match.group(0)

    # Step 2: Parse JSON string into dict
    try:
        parsed_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON: {e}\nRaw output was:\n{json_str}")

    # Step 3: Validate using Pydantic
    try:
        validated_obj = schema_model.model_validate(parsed_data)
    except Exception as e:
        raise ValueError(f"Validation error: {e}\nParsed data was:\n{parsed_data}")

    return validated_obj

class User(BaseModel):
    """A user profile with contact details."""
    # Define the fields for the user profile
    name: str
    surname: str
    age: int
    email: str
    phone: str
    social_accounts: Dict[str, str]

user_statement = "Ram kumar is a softwaree engineer of 26 years old. He lives in Bangalore, India. His email is ram@social. com and his phone number is 1234567890. He has a bluesky account with the username ramkumar and an instagram account with the username ramkumar_26."
# from pprint import pprint
# pprint(User.model_json_schema())

completion = client.chat.completions.create(
    # model="deepseek-r1-distill-llama-70b",
    model ="qwen/qwen3-32b",
    messages=[
        {
            "role": "user",
            # "content": f"please extract from the following text the contact details of the user using below schema\n\n##schema {User.model_json_schema()}```text\n" + user_statement + "\n```",
            "content": f"Extract the contact details from the text. Respond ONLY with valid JSON that matches this schema: {User.model_json_schema()}\nText:\n{user_statement}"

        }
    ],
    temperature=0.6,
    # max_completion_tokens=1024,
    top_p=0.95,
    stream= False,
    # reasoning_format="raw"
    reasoning_effort="none",  # parsed, raw, hidden, none
)

print(completion.choices[0].message.content)
# Example usage:
validated_user = extract_and_validate_json(completion, User)
print(validated_user.model_dump_json(indent=2))

# ```json
# {
#   "name": "Ram",
#   "surname": "kumar",
#   "age": 26,
#   "email": "ram@social.com",
#   "phone": "1234567890",
#   "social_accounts": {
#     "bluesky": "ramkumar",
#     "instagram": "ramkumar_26"
#   }
# }
# ```
# {
#   "name": "Ram",
#   "surname": "kumar",
#   "age": 26,
#   "email": "ram@social.com",
#   "phone": "1234567890",
#   "social_accounts": {
#     "bluesky": "ramkumar",
#     "instagram": "ramkumar_26"
#   }
# }






