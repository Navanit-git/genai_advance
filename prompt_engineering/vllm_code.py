from openai import OpenAI
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id

# messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
messages = [{"role": "user", "content": "How many 'r' are there in strawberry?"}]

# messages=[{"role": "user", "content": "Give me a short introduction to large language models."},]
# chat_response = client.chat.completions.create(
#     model=model,
#     messages = messages,
#     max_tokens=300,
#     temperature=0.6,
#     top_p=0.95,
#     extra_body={
#         "top_k": 20,
#         "chat_template_kwargs": {"enable_thinking": False}
#     },
# )
# print("Chat response:", chat_response)


# stream = client.chat.completions.create(model=model,
#                                         messages=messages,
#                                         stream=True,
#                                         extra_body={"chat_template_kwargs": {"enable_thinking": False}},)

# print("client: Start streaming chat completions...")
# printed_reasoning_content = False
# printed_content = False

# for chunk in stream:
#     reasoning_content = None
#     content = None
#     # Check the content is reasoning_content or content
#     if hasattr(chunk.choices[0].delta, "reasoning_content"):
#         reasoning_content = chunk.choices[0].delta.reasoning_content
#     elif hasattr(chunk.choices[0].delta, "content"):
#         content = chunk.choices[0].delta.content

#     if reasoning_content is not None:
#         if not printed_reasoning_content:
#             printed_reasoning_content = True
#             print("reasoning_content:", end="", flush=True)
#         print(reasoning_content, end="", flush=True)
#     elif content is not None:
#         if not printed_content:
#             printed_content = True
#             print("\ncontent:", end="", flush=True)
#         # Extract and print the content
#         print(content, end="", flush=True)


tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location", "unit"]
        }
    }
}]

response = client.chat.completions.create(
    model=client.models.list().data[0].id,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=tools,
    tool_choice="auto",
    extra_body={"chat_template_kwargs": {"enable_thinking": False}}
)

print(response)
# tool_call = response.choices[0].message.tool_calls[0].function

print(f"reasoning_content: {response.choices[0].message.reasoning_content}")
# print(f"Function called: {tool_call.name}")
# print(f"Arguments: {tool_call.arguments}")


#  result = chat_completion_from_url.choices[0].message.content

# ((gen_env) ) nav_wsl@nav:~/code$ vllm serve Qwen/Qwen3-0.6B  --reasoning-parser qwen3 --max-model-len 4096  --enable-auto-tool-choice --tool-call-parser hermes --quantization bitsandbytes



#  vllm serve Qwen/Qwen3-4B  --reasoning-parser qwen3 --max-model-len 4096  --enable-auto-tool-choice --tool-call-parser hermes --quantization awq --gpu_memory_utilization 0.9 --quantization bitsandbytes --load-format bitsandbytes 


# Qwen/Qwen3-4B-AWQ --Got OOM
# Qwen/Qwen3-4B-MLX-4bit -- For apple models
#  max_model_len, --max_num_seqs 1

# the quantization method fp8 is not supported for the current GPU.