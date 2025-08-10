#using xml https://python.langchain.com/docs/how_to/output_parser_xml/
#using yaml https://python.langchain.com/docs/how_to/output_parser_yaml/
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
                model="qwen/qwen3-32b",
                # model="deepseek-r1-distill-llama-70b",
               api_key= groq_key_1,  
               reasoning_effort = "none"
               )

from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate

actor_query = "Generate the shortened filmography for Tom Hanks."

# output = llm.invoke(
#     f"""{actor_query}
# Please enclose the movies in <movie></movie> tags"""
# )

# print(output.content)

# Here’s a shortened filmography for Tom Hanks, with movies enclosed in `<movie>` tags:

# - <movie>Splash</movie> (1984)  
# - <movie>Big</movie> (1988)  
# - <movie>A League of Their Own</movie> (1992)  
# - <movie>Forrest Gump</movie> (1994)  
# - <movie>Apollo 13</movie> (1995)  
# - <movie>Saving Private Ryan</movie> (1998)  
# - <movie>The Green Mile</movie> (1999)  
# - <movie>Cast Away</movie> (2000)  
# - <movie>The Da Vinci Code</movie> (2006)  
# - <movie>Sully</movie> (2016)  
# - <movie>News of the World</movie> (2020)  
# - <movie>Elvis</movie> (2022)  

# Let me know if you'd like a more extensive list!

parser = XMLOutputParser()

# We will add these instructions to the prompt below
# parser.get_format_instructions()
# 'The output should be formatted as a XML file.\n1. Output should conform to the tags below. \n2. If tags are not given, make them on your own.\n3. Remember to always open and close all the tags.\n\nAs an example, for the tags ["foo", "bar", "baz"]:\n1. String "<foo>\n   <bar>\n      <baz></baz>\n   </bar>\n</foo>" is a well-formatted instance of the schema. \n2. String "<foo>\n   <bar>\n   </foo>" is a badly-formatted instance.\n3. String "<foo>\n   <tag>\n   </tag>\n</foo>" is a badly-formatted instance.\n\nHere are the output tags:\n\`\`\`\nNone\n\`\`\`'

prompt = PromptTemplate(
    template="""{query}\n{format_instructions}""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# chain = prompt | llm | parser

# output = chain.invoke({"query": actor_query})
# print(output)
# {'filmography': [{'movie': [{'title': 'Forrest Gump'}, {'year': '1994'}, {'role': 'Forrest Gump'}, {'director': 'Robert Zemeckis'}]}, {'movie': [{'title': 'Cast Away'}, {'year': '2000'}, {'role': 'Chuck Noland'}, {'director': 'Robert Zemeckis'}]}, {'movie': [{'title': 'Apollo 13'}, {'year': '1995'}, {'role': 'Jim Lovell'}, {'director': 'Ron Howard'}]}, {'movie': [{'title': 'Saving Private Ryan'}, {'year': '1998'}, {'role': 'Captain John Miller'}, {'director': 'Steven Spielberg'}]}, {'movie': [{'title': 'The Da Vinci Code'}, {'year': '2006'}, {'role': 'Robert Langdon'}, {'director': 'Ron Howard'}]}, {'movie': [{'title': 'Sully'}, {'year': '2016'}, {'role': 'Chesley Sullenberger'}, {'director': 'Clint Eastwood'}]}, {'movie': [{'title': 'Big'}, {'year': '1988'}, {'role': 'Josh Baskin'}, {'director': 'Penny Marshall'}]}, {'movie': [{'title': 'A League of Their Own'}, {'year': '1992'}, {'role': 'Jimmy Dugan'}, {'director': 'Penny Marshall'}]}, {'movie': [{'title': 'Philadelphia'}, {'year': '1993'}, {'role': 'Andrew Beckett'}, {'director': 'Jonathan Demme'}]}, {'movie': [{'title': 'The Polar Express'}, {'year': '2004'}, {'role': 'The Conductor'}, {'director': 'Robert Zemeckis'}]}, {'movie': [{'title': 'Captain Phillips'}, {'year': '2013'}, {'role': 'Captain Richard Phillips'}, {'director': 'Paul Greengrass'}]}, {'movie': [{'title': 'Bridge of Spies'}, {'year': '2015'}, {'role': 'James B. Donovan'}, {'director': 'Steven Spielberg'}]}, {'movie': [{'title': 'The Post'}, {'year': '2017'}, {'role': 'Ben Bradlee'}, {'director': 'Steven Spielberg'}]}, {'movie': [{'title': 'Toy Story'}, {'year': '1995'}, {'role': 'Woody'}, {'director': 'John Lasseter'}]}, {'movie': [{'title': 'Inferno'}, {'year': '2016'}, {'role': 'Robert Langdon'}, {'director': 'Ron Howard'}]}, {'movie': [{'title': 'News of the World'}, {'year': '2020'}, {'role': 'Captain Jefferson Kyle Kidd'}, {'director': 'Paul Greengrass'}]}, {'movie': [{'title': 'Elvis'}, {'year': '2022'}, {'role': 'Colonel Tom Parker'}, {'director': 'Baz Luhrmann'}]}]}

## adding tags 
parser = XMLOutputParser(tags=["movies", "actor", "film", "name", "genre"])

# We will add these instructions to the prompt below
# parser.get_format_instructions()
# 'The output should be formatted as a XML file.\n1. Output should conform to the tags below. \n2. If tags are not given, make them on your own.\n3. Remember to always open and close all the tags.\n\nAs an example, for the tags ["foo", "bar", "baz"]:\n1. String "<foo>\n   <bar>\n      <baz></baz>\n   </bar>\n</foo>" is a well-formatted instance of the schema. \n2. String "<foo>\n   <bar>\n   </foo>" is a badly-formatted instance.\n3. String "<foo>\n   <tag>\n   </tag>\n</foo>" is a badly-formatted instance.\n\nHere are the output tags:\n\`\`\`\n[\'movies\', \'actor\', \'film\', \'name\', \'genre\']\n\`\`\`'

prompt = PromptTemplate(
    template="""{query}\n{format_instructions}""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


# chain = prompt | llm | parser

# output = chain.invoke({"query": actor_query})

# print(output)

# {'movies': [{'actor': 'Tom Hanks'}, {'film': [{'name': 'Forrest Gump'}, {'genre': 'Drama'}]}, {'film': [{'name': 'Cast Away'}, {'genre': 'Adventure/Drama'}]}, {'film': [{'name': 'Apollo 13'}, {'genre': 'Drama/Adventure'}]}, {'film': [{'name': 'Saving Private Ryan'}, {'genre': 'War/Drama'}]}, {'film': [{'name': 'The Da Vinci Code'}, {'genre': 'Mystery/Thriller'}]}]}

##yaml output parser

from langchain.output_parsers import YamlOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

# And a query intented to prompt a language model to populate the data structure.
joke_query = "Tell me a joke."

# Set up a parser + inject instructions into the prompt template.
parser = YamlOutputParser(pydantic_object=Joke)
# print(parser.get_format_instructions())

#  "Human: Answer the user query.\nThe output should be formatted as a YAML instance that conforms to the given JSON schema below.\n\n# Examples\n## Schema\n```\n{\"title\": \"Players\", \"description\": \"A list of players\", \"type\": \"array\", \"items\": {\"$ref\": \"#/definitions/Player\"}, \"definitions\": {\"Player\": {\"title\": \"Player\", \"type\": \"object\", \"properties\": {\"name\": {\"title\": \"Name\", \"description\": \"Player name\", \"type\": \"string\"}, \"avg\": {\"title\": \"Avg\", \"description\": \"Batting average\", \"type\": \"number\"}}, \"required\": [\"name\", \"avg\"]}}}\n```\n## Well formatted instance\n```\n- name: John Doe\n  avg: 0.3\n- name: Jane Maxfield\n  avg: 1.4\n```\n\n## Schema\n```\n{\"properties\": {\"habit\": { \"description\": \"A common daily habit\", \"type\": \"string\" }, \"sustainable_alternative\": { \"description\": \"An environmentally friendly alternative to the habit\", \"type\": \"string\"}}, \"required\": [\"habit\", \"sustainable_alternative\"]}\n```\n## Well formatted instance\n```\nhabit: Using disposable water bottles for daily hydration.\nsustainable_alternative: Switch to a reusable water bottle to reduce plastic waste and decrease your environmental footprint.\n```\n\nPlease follow the standard YAML formatting conventions with an indent of 2 spaces and make sure that the data types adhere strictly to the following JSON schema:\n```\n{\"properties\": {\"setup\": {\"description\": \"question to set up a joke\", \"title\": \"Setup\", \"type\": \"string\"}, \"punchline\": {\"description\": \"answer to resolve the joke\", \"title\": \"Punchline\", \"type\": \"string\"}}, \"required\": [\"setup\", \"punchline\"]}\n```\n\nMake sure to always enclose the YAML output in triple backticks (```). Please do not add anything other than valid YAML output!\nTell me a joke."
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

print(chain.invoke({"query": joke_query}))

# setup='Why did the scarecrow win an award?' punchline='Because he was outstanding in his field!'
