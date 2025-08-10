from langchain_groq import ChatGroq
from langchain_core.callbacks import StdOutCallbackHandler
from langchain.globals import set_debug, set_verbose
set_debug(True)
set_verbose(True)
import json
with open("keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]
llm = ChatGroq(model="qwen/qwen3-32b",
               api_key= groq_key_1,  
               reasoning_effort = "none"
               )


# from langchain_core.tools import tool


# @tool
# def get_weather(location: str) -> str:
#     """Get the weather from a location."""

#     return "Sunny."


# llm_with_tools = llm.bind_tools([get_weather])

# response = llm_with_tools.invoke("What's the weather in San Francisco, CA?")
# print("-----------------------\n\n", response)
# print(response.content)
#  content='' additional_kwargs={'reasoning_content': "Okay, the user is asking for the weather in San Francisco, CA. Let me check the tools available. There's a function called get_weather that takes a location parameter. The required parameter is location, which should be a string. San Francisco, CA is the location they mentioned. I need to call get_weather with that location. Make sure the arguments are correctly formatted as JSON. Let me structure the tool_call with the name and arguments.\n", 'tool_calls': [{'id': 'jsqt2vgb0', 'function': {'arguments': '{"location":"San Francisco, CA"}', 'name': 'get_weather'}, 'type': 'function'}]} response_metadata={'token_usage': {'completion_tokens': 116, 'prompt_tokens': 156, 'total_tokens': 272, 'completion_time': 0.171657137, 'prompt_time': 0.095574827, 'queue_time': 0.045249182, 'total_time': 0.267231964}, 'model_name': 'qwen/qwen3-32b', 'system_fingerprint': 'fp_5cf921caa2', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None} id='run--1b89adc6-69ac-4693-b977-7b8f48427bfe-0' tool_calls=[{'name': 'get_weather', 'args': {'location': 'San Francisco, CA'}, 'id': 'jsqt2vgb0', 'type': 'tool_call'}] usage_metadata={'input_tokens': 156, 'output_tokens': 116, 'total_tokens': 272}

# from langchain_core.output_parsers import StrOutputParser

# chain = llm_with_tools | StrOutputParser()

# response = chain.invoke("What's the weather in San Francisco, CA?")
# print(response)


from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, model_validator

# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

    # You can add custom validation logic easily with Pydantic.
    @model_validator(mode="before")
    @classmethod
    def question_ends_with_question_mark(cls, values: dict) -> dict:
        setup = values.get("setup")
        if setup and setup[-1] != "?":
            raise ValueError("Badly formed question!")
        return values

# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# And a query intended to prompt a language model to populate the data structure.
# prompt_and_model = prompt | llm
# output = prompt_and_model.invoke({"query": "Tell me a joke."})
# value = parser.invoke(output)
# print("-------------\n\n",value)

# {
#   "prompts": [
#     "Human: Answer the user query.\nThe output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {\"properties\": {\"foo\": {\"title\": \"Foo\", \"description\": \"a list of strings\", \"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"required\": [\"foo\"]}\nthe object {\"foo\": [\"bar\", \"baz\"]} is a well-formatted instance of the schema. The object {\"properties\": {\"foo\": [\"bar\", \"baz\"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{\"properties\": {\"setup\": {\"description\": \"question to set up a joke\", \"title\": \"Setup\", \"type\": \"string\"}, \"punchline\": {\"description\": \"answer to resolve the joke\", \"title\": \"Punchline\", \"type\": \"string\"}}, \"required\": [\"setup\", \"punchline\"]}\n```\nTell me a joke."
#   ]
# }


## Without PydanticOutputParser
from langchain_core.output_parsers import JsonOutputParser
joke_query = "Tell me a joke."
parser = JsonOutputParser()
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
chain = prompt | llm | parser

chain.invoke({"query": joke_query})

# "content": "```json\n{\n  \"joke\": \"Why did the math book look sad? Because it had too many problems.\"\n}\n```",

# {
#   "joke": "Why did the math book look sad? Because it had too many problems."
# }


