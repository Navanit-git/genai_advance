# used this link https://python.langchain.com/docs/how_to/structured_output/ 
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
llm = ChatGroq(
                # model="qwen/qwen3-32b",
                model="deepseek-r1-distill-llama-70b",
               api_key= groq_key_1,  
            #    reasoning_effort = "none"
               )


#pydantic class

from typing import Optional

from pydantic import BaseModel, Field


# Pydantic
class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )


# structured_llm = llm.with_structured_output(Joke)

# structured_llm.invoke("Tell me a joke about cats")

## Multiple messages

from typing import Union


class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )


class ConversationalResponse(BaseModel):
    """Respond in a conversational manner. Be kind and helpful."""

    response: str = Field(description="A conversational response to the user's query")


class FinalResponse(BaseModel):
    final_output: Union[Joke, ConversationalResponse]


# structured_llm = llm.with_structured_output(FinalResponse)

# structured_llm.invoke("Tell me a joke about cats")


## few short prompting

from langchain_core.prompts import ChatPromptTemplate

from typing_extensions import Annotated, TypedDict


# TypedDict
class Joke(TypedDict):
    """Joke to tell user."""

    setup: Annotated[str, ..., "The setup of the joke"]
    punchline: Annotated[str, ..., "The punchline of the joke"]
    rating: Annotated[Optional[int], None, "How funny the joke is, from 1 to 10"]


structured_llm = llm.with_structured_output(Joke)

system = """You are a hilarious comedian. Your specialty is knock-knock jokes. \
Return a joke which has the setup (the response to "Who's there?") and the final punchline (the response to "<setup> who?").

Here are some examples of jokes:

example_user: Tell me a joke about planes
example_assistant: {{"setup": "Why don't planes ever get tired?", "punchline": "Because they have rest wings!", "rating": 2}}

example_user: Tell me another joke about planes
example_assistant: {{"setup": "Cargo", "punchline": "Cargo 'vroom vroom', but planes go 'zoom zoom'!", "rating": 10}}

example_user: Now about caterpillars
example_assistant: {{"setup": "Caterpillar", "punchline": "Caterpillar really slow, but watch me turn into a butterfly and steal the show!", "rating": 5}}"""

# prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{input}")])

# few_shot_structured_llm = prompt | structured_llm
# few_shot_structured_llm.invoke("what's something funny about woodpeckers")

# Using prompts with structured output
# structured_llm = llm.with_structured_output(None, method="json_mode")

# print(structured_llm.invoke(
#     "Tell me a joke about cats, respond in JSON with `setup` and `punchline` keys"
# ))
# {'setup': "Why don't cats play poker in the jungle?", 'punchline': 'Too many cheetahs.'}
## RAW OUTPUT
# structured_llm = llm.with_structured_output(Joke, include_raw=True)

# print(structured_llm.invoke("Tell me a joke about cats"))

# {'raw': AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'jxmd1kk4a', 'function': {'arguments': '{"punchline":"Too many cheetahs.","rating":7,"setup":"Why don\'t cats play poker in the jungle?"}', 'name': 'Joke'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 47, 'prompt_tokens': 219, 'total_tokens': 266, 'completion_time': 0.087054812, 'prompt_time': 0.013944524, 'queue_time': 0.051501794, 'total_time': 0.100999336}, 'model_name': 'qwen/qwen3-32b', 'system_fingerprint': 'fp_5cf921caa2', 'service_tier': 'on_demand', 'reasoning_effort': 'none', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run--c8e8a1b1-e0f5-4042-83ea-d02aa7f9747b-0', tool_calls=[{'name': 'Joke', 'args': {'punchline': 'Too many cheetahs.', 'rating': 7, 'setup': "Why don't cats play poker in the jungle?"}, 'id': 'jxmd1kk4a', 'type': 'tool_call'}], usage_metadata={'input_tokens': 219, 'output_tokens': 47, 'total_tokens': 266}), 'parsed': {'punchline': 'Too many cheetahs.', 'rating': 7, 'setup': "Why don't cats play poker in the jungle?"}, 'parsing_error': None}


## format instructions
from typing import List

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class Person(BaseModel):
    """Information about a person."""

    name: str = Field(..., description="The name of the person")
    height_in_meters: float = Field(
        ..., description="The height of the person expressed in meters."
    )


class People(BaseModel):
    """Identifying information about all people in a text."""

    people: List[Person]


# Set up a parser
parser = PydanticOutputParser(pydantic_object=People)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user query. Wrap the output in `json` tags\n{format_instructions}",
        ),
        ("human", "{query}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

query = "Anna is 23 years old and she is 6 feet tall"

# print(prompt.invoke({"query": query}).to_string())

# chain = prompt | llm | parser

# print(chain.invoke({"query": query}))

# people=[Person(name='Anna', height_in_meters=1.8288)]


##custom parsing 

import json
import re
from typing import List

from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class Person(BaseModel):
    """Information about a person."""

    name: str = Field(..., description="The name of the person")
    height_in_meters: float = Field(
        ..., description="The height of the person expressed in meters."
    )


class People(BaseModel):
    """Identifying information about all people in a text."""

    people: List[Person]


# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user query. Output your answer as JSON that  "
            "matches the given schema: \`\`\`json\n{schema}\n\`\`\`. "
            "Make sure to wrap the answer in \`\`\`json and \`\`\` tags",
        ),
        ("human", "{query}"),
    ]
).partial(schema=People.model_json_schema())


# Custom parser
def extract_json(message: AIMessage) -> List[dict]:
    """Extracts JSON content from a string where JSON is embedded between \`\`\`json and \`\`\` tags.

    Parameters:
        text (str): The text containing the JSON content.

    Returns:
        list: A list of extracted JSON strings.
    """
    text = message.content
    # Define the regular expression pattern to match JSON blocks
    pattern = r"\`\`\`json(.*?)\`\`\`"

    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the list of matched JSON strings, stripping any leading or trailing whitespace
    try:
        return [json.loads(match.strip()) for match in matches]
    except Exception:
        raise ValueError(f"Failed to parse: {message}")
    
query = "Anna is 23 years old and she is 6 feet tall"

# print(prompt.format_prompt(query=query).to_string())

chain = prompt | llm | extract_json

# print(chain.invoke({"query": query}))

# [{'people': [{'name': 'Anna', 'height_in_meters': 1.83}]}]