# from langchain_community.llms import VLLMOpenAI

# llm = VLLMOpenAI(
#     openai_api_key="EMPTY",
#     openai_api_base="http://localhost:8000/v1",
#     model_name="tiiuae/falcon-7b",
#     model_kwargs={"stop": ["."]},
# )
# print(llm.invoke("Rome is"))


from langchain_groq import ChatGroq
import json
with open("keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    api_key= groq_key_1
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Hindi. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)

# content="J'aime la programmation." additional_kwargs={'reasoning_content': 'Okay, so I need to translate the sentence "I love programming." into French. Let me think about how to approach this. '} response_metadata={'token_usage': {'completion_tokens': 422, 'prompt_tokens': 23, 'total_tokens': 445, 'completion_time': 1.68260374, 'prompt_time': 0.011417025, 'queue_time': 0.045450055, 'total_time': 1.6940207649999999}, 'model_name': 'deepseek-r1-distill-llama-70b', 'system_fingerprint': 'fp_1bbe7845ec', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None} id='run--262ce727-8bbb-469c-9128-14be43cbf0fa-0' usage_metadata={'input_tokens': 23, 'output_tokens': 422, 'total_tokens': 445}

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
value = chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)
print(value)


# content='The translation of "I love programming" into German is "Ich liebe das Programmieren."' additional_kwargs={'reasoning_content': 'Okay, so I need to translate the sentence "I love programming." into German. Hmm, let\'s break this down.  "I love programming" becomes "Ich liebe das Programmieren." That should be the right translation.\n'} response_metadata={'token_usage': {'completion_tokens': 602, 'prompt_tokens': 18, 'total_tokens': 620, 'completion_time': 2.488808807, 'prompt_time': 0.010933095, 'queue_time': 0.268564543, 'total_time': 2.4997419020000002}, 'model_name': 'deepseek-r1-distill-llama-70b', 'system_fingerprint': 'fp_5d7bb96f85', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None} id='run--cd1798df-017d-4ee9-ade6-3341fce467ae-0' usage_metadata={'input_tokens': 18, 'output_tokens': 602, 'total_tokens': 620}