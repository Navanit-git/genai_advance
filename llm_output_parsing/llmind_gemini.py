import json 

with open("../keys.json") as f:
    api_key = json.load(f)


gemini_key_1 =api_key["google_api_key_1"]
gemini_key_2 =api_key["google_api_key_2"]
gemini_key_3 =api_key["google_api_key_3"]

from llama_index.llms.google_genai import GoogleGenAI

llm = GoogleGenAI(
    model="gemini-2.0-flash",
    api_key=gemini_key_1,  # uses GOOGLE_API_KEY env var by default
    # api_key="some key",  # uses GOOGLE_API_KEY env var by default
)

resp = llm.complete("Who is Paul Graham?")
print(resp)