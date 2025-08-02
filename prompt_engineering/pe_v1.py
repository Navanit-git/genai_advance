import os
import openai
import json 

with open("keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]

from groq import Groq

client = Groq(
    api_key=groq_key_1,
)

#instruction prompting
prompt_1 = """A user has input their first and last name into a form. We don't know in which order their first name and last name are, but we need it to be in this format '[Last name], [First name]'.
Please convert the following name in the expected format: Charlie Brown"""

prompt_2= """Read the following sales email. Remove any personally identifiable information (PII), and replace it with the appropriate placeholder. For example, replace the name "John Doe" with "[NAME]".
Hi John,
I'm writing to you because I noticed you recently purchased a new car. I'm a salesperson at a local dealership (Cheap Dealz), and I wanted to let you know that we have a great deal on a new car. If you're interested, please let me know.
Thanks,
Jimmy Smith
Phone: 410-805-2345 Email: jimmysmith@cheapdealz.com"""


# role prompting

prompt_3 = "You are a communications specialist. Draft an email to your client advising them about a delay in the delivery schedule due to logistical problems."

prompt_4=  """You are a brilliant mathematician who can solve any problem in the world. Attempt to solve the following problem:
What is 100*100/400*56?"""

# role + Instruction prompting

prompt_5 = """You are a historian specializing in the American Civil War. Write a brief summary of the key events and outcomes of the war."""

# Instruction + Context

prompt_6 = """Summarize this email in one sentence.
Dear team, thank you for organizing the community event. It was a great success thanks to your hard work."""

completion = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[
        {
            "role": "user",
            "content":prompt_4 ,
        }
    ],
    temperature=0.6,
    # max_completion_tokens=1024,
    reasoning_effort="none",

    top_p=0.95,
)

print(completion.choices[0].message.content)




