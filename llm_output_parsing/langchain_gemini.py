from langchain_google_genai import GoogleGenerativeAI
from langchain_core.callbacks import StdOutCallbackHandler
from langchain.globals import set_debug, set_verbose
set_debug(True)
set_verbose(True)
import json 

with open("keys.json") as f:
    api_key = json.load(f)


gemini_key_1 =api_key["google_api_key_1"]
gemini_key_2 =api_key["google_api_key_2"]
gemini_key_3 =api_key["google_api_key_3"]


llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=gemini_key_1)
# print(
#     llm.invoke(
#         "What are some of the pros and cons of Python as a programming language?"
#     )
# )

from langchain_core.prompts import PromptTemplate

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)

chain = prompt | llm

question = "How much is 2+2?"
value = chain.invoke({"question": question},callbacks=[StdOutCallbackHandler()],)
print("-----------------------\n\n",value)