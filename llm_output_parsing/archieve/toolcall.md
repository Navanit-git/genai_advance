# Tool Calling for LLMs: A Comprehensive Guide for Industrial Applications

## Introduction
Tool Calling is a transformative capability that enables Large Language Models (LLMs) to interact with external tools, APIs, or systems, extending their functionality beyond text generation to tasks like data retrieval, calculations, and automation. Unlike Function Calling, which focuses on invoking predefined functions, Tool Calling encompasses a broader range of external resources, such as web search, database queries, or third-party APIs. As of August 6, 2025, Tool Calling is critical for industrial applications, including chatbots, virtual assistants, and workflow automation systems, where LLMs need to perform actionable tasks in real-time.

This guide provides a modular approach to mastering Tool Calling, covering foundational concepts, implementation techniques for both large and small models, advanced strategies, and real-world applications. It emphasizes practical exercises with diverse tools, such as web search, database queries, and external APIs, to ensure applicability in industrial settings. Whether you’re building a customer support bot or automating a supply chain process, this guide equips you with the skills to leverage Tool Calling effectively.

## Module 1: Basics of Tool Calling

### Concepts
- **Definition of Tool Calling**: Tool Calling allows LLMs to analyze user queries, select appropriate external tools or APIs, and generate structured outputs (typically JSON) specifying the tool and its arguments. The application then executes the tool, not the LLM.
- **Difference from Function Calling**: Function Calling is a subset of Tool Calling, focusing on predefined functions, while Tool Calling includes any external resource, such as APIs, databases, or custom tools.
- **Importance**: Enables LLMs to perform real-world tasks like fetching weather data, querying databases, or executing calculations, making them versatile for industrial applications.
- **Tool Schemas**: Define the tool’s name, description, and parameters to guide the LLM in selecting and using the tool correctly.
- **Supported Tools**: Examples include:
  - **Calculator**: Performs mathematical operations.
  - **Weather API**: Fetches real-time weather data.
  - **Database Query**: Retrieves data from a database.
  - **Web Search**: Searches the internet for information.
  - **Calendar API**: Schedules events or retrieves calendar data.

### Practice
1. **Setup**: Install required libraries: `pip install langchain openai pydantic guardrails-ai`.
2. **Define Simple Tools**: Create tools like a calculator and a weather API.
3. **Use LangChain’s Agent Framework**: Initialize an agent with `initialize_agent` to select and call tools based on user queries.
4. **Test Case**: Query the LLM with “What’s the temperature in Delhi?” and verify the tool call.

### Example: Basic Tool Calling with LangChain
```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

# Define tools
def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"Weather in {city}: Sunny, 25°C"

def calculate(expression: str) -> float:
    """Perform a calculation."""
    return eval(expression)  # Use cautiously in production

tools = [
    Tool(name="get_weather", func=get_weather, description="Get weather for a city"),
    Tool(name="calculate", func=calculate, description="Perform a calculation")
]

# Initialize agent
llm = OpenAI()
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Run query
result = agent.run("What's the temperature in Delhi?")
print(result)  # Output: Weather in Delhi: Sunny, 25°C
```

### Resources
- [LangChain Agents Documentation](https://python.langchain.com/docs/modules/agents/)
- [OpenAI Tool Calling Guide](https://platform.openai.com/docs/guides/tool-calling)
- [Tool Calling in LLMs](https://www.analyticsvidhya.com/blog/2024/08/tool-calling-in-llms/)

### Industry Application
- **Customer Support Bot**: Fetch order details from a database or check inventory levels using tool calls. For example, a query like “What’s the status of order #123?” triggers a database query tool to retrieve the status.

## Module 2: Advanced Tool Calling Techniques

### Concepts
- **Multi-Tool Selection**: Enable the LLM to choose from multiple tools based on the query’s intent, enhancing flexibility.
- **Chaining Tools**: Use the output of one tool as input for another to handle complex, multi-step tasks.
- **Error Handling and Retries**: Manage tool call failures, such as API downtime or invalid arguments, with robust validation and retry mechanisms.
- **Integrating with Real APIs**: Connect tools to external services like OpenWeatherMap or Google Calendar for dynamic data retrieval.
- **Diverse Tools**:
  - **Web Search Tool**: Fetches information from the internet.
  - **Price Check Tool**: Retrieves product prices from an e-commerce API.
  - **Email Sender**: Sends emails via an SMTP server.
  - **File Reader**: Reads data from files or databases.
  - **Translation API**: Translates text using services like Google Translate.

### Practice
1. **Define Complex Tools**: Create tools like a web search tool, price check tool, and email sender.
2. **Implement Chaining**: Allow the LLM to chain tools, e.g., search for a product and then check its price.
3. **Add Error Handling**: Use try-except blocks or Guardrails AI to manage failed tool calls.
4. **Test Case**: Query with “What’s the price of the latest iPhone?” to trigger a web search followed by a price check.

### Example: Chaining Tools with LangChain
```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

# Define tools
def search_product(query: str) -> str:
    """Search for a product."""
    return f"Found product: {query}"

def get_price(product: str) -> str:
    """Get the price of a product."""
    return f"Price of {product}: $999"

tools = [
    Tool(name="search_product", func=search_product, description="Search for a product"),
    Tool(name="get_price", func=get_price, description="Get the price of a product")
]

# Initialize agent
llm = OpenAI()
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Run query
result = agent.run("What's the price of the latest iPhone?")
print(result)  # Output: Found product: latest iPhone; Price of latest iPhone: $999
```

### Resources
- [LangChain Tool Calling Examples](https://python.langchain.com/docs/use_cases/agents)
- [Griptape Documentation](https://docs.griptape.ai/)
- [Tool Calling with LLMs](https://blog.promptlayer.com/tool-calling-with-llms-how-and-when-to-use-it/)

### Industry Application
- **Intelligent Assistant**: Perform multi-step tasks like booking a flight and then a hotel by chaining a travel API and a booking API.

## Module 3: Tool Calling with Small Models

### Concepts
- **Challenges with Small Models**: Small models (e.g., Mistral-7B, Llama 3.1) often lack native Tool Calling support, requiring structured output methods to simulate this functionality.
- **Structured Output Approach**: Prompt the LLM to generate JSON specifying the tool name and arguments, then parse and execute the tool.
- **Specialized Small Models**: Models like Mistral-7B-Instruct or LLMWare’s SLIM models are fine-tuned for structured output tasks, improving Tool Calling performance.
- **Validation and Error Handling**: Use Pydantic or Guardrails AI to validate outputs and handle inconsistencies common in smaller models.

### Practice
1. **Select a Small Model**: Use Mistral-7B-Instruct or Llama 3.1 from Hugging Face.
2. **Design Prompt**: Instruct the LLM to return JSON with tool name and arguments.
3. **Parse Output**: Use LangChain’s `StructuredOutputParser` or Instructor to parse JSON.
4. **Execute Tool**: Call the corresponding tool and handle errors.
5. **Test Case**: Query with “What’s the weather in London?” and verify the generated tool call.

### Example: Tool Calling with Small Model (Mistral-7B)
```python
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from pydantic import BaseModel, ValidationError

# Define Pydantic model for validation
class WeatherToolCall(BaseModel):
    tool: str
    arguments: dict

# Define function schema
response_schemas = [
    ResponseSchema(name="tool", description="The name of the tool to call", type="string"),
    ResponseSchema(name="arguments", description="The arguments for the tool", type="object")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

# Define prompt
prompt = PromptTemplate(
    template="You are an assistant that can call tools. If the user asks for weather, return a JSON object with 'tool' and 'arguments'. User: {query}\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions}
)

# Load small model
llm = HuggingFacePipeline.from_model_id(model_id="mistralai/Mistral-7B-Instruct-v0.1", task="text-generation")

# Combine prompt and parser
chain = prompt | llm | output_parser

# Define get_weather function
def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"Weather in {city}: Sunny, 25°C"

# Invoke chain
result = chain.invoke({"query": "What's the weather in London?"})
print(result)  # Output: {'tool': 'get_weather', 'arguments': {'city': 'London'}}

# Validate and execute
try:
    tool_call = WeatherToolCall(**result)
    if tool_call.tool == "get_weather":
        print(get_weather(tool_call.arguments["city"]))
except ValidationError:
    print("Invalid tool call, retrying...")
```

### Resources
- [Mistral AI Function Calling](https://docs.mistral.ai/capabilities/function_calling/)
- [Instructor GitHub](https://github.com/jxnl/instructor)
- [Local LLM Tool Calling](https://www.docker.com/blog/local-llm-tool-calling-a-practical-evaluation/)

### Industry Application
- **Lightweight Chatbot**: Use a small model to perform tasks like fetching weather or news, reducing costs for resource-constrained environments.

## Module 4: Industrial Applications of Tool Calling

### Concepts
- **Real-World Use Cases**:
  - **Chatbots**: Fetch real-time data (e.g., order status, weather) or perform actions (e.g., sending emails).
  - **Data Extraction**: Query databases to extract structured data from unstructured text.
  - **Workflow Automation**: Orchestrate multi-step processes, such as inventory checks followed by reordering.
  - **API Integration**: Convert natural language queries into API calls for seamless system integration.
- **Diverse Tools**:
  - **Inventory Management Tool**: Checks stock levels in a database.
  - **Notification Tool**: Sends alerts via email or SMS.
  - **Analytics Tool**: Performs data analysis using external services.
  - **Translation Tool**: Translates text using APIs like Google Translate.
  - **Search Engine Tool**: Queries a search engine for real-time information.
- **Challenges**:
  - **Consistency**: Small models may produce inconsistent outputs, requiring robust validation.
  - **Latency**: API calls can introduce delays; optimization is critical for real-time applications.
  - **Security**: Sanitize inputs and outputs to prevent injection attacks or data leaks.
- **Best Practices**:
  - Use Pydantic or Guardrails AI for output validation.
  - Implement retry logic for failed tool calls.
  - Test with real-world data to ensure reliability.
  - Optimize latency by caching frequent API responses.

### Practice
- **Project: Customer Support Bot**
  - **Goal**: Build a bot that retrieves order status and shipping information using tool calling.
  - **Tools**: Database query for order status, API for shipping information.
  - **Test Case**: Query with “What’s the status of my order #123?” and verify the tool call.
- **Project: Multi-Tool Assistant**
  - **Goal**: Create an assistant that handles weather, calculations, and scheduling tasks.
  - **Tools**: Weather API, calculator, calendar API.
  - **Test Case**: Query with “Calculate the temperature in London tomorrow plus 100” and verify the multi-step process.

### Example Project: Customer Support Bot
```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

# Define tools
def get_order_status(order_id: str) -> str:
    """Get order status from a database."""
    return f"Order #{order_id}: Shipped"

def get_shipping_info(order_id: str) -> str:
    """Get shipping information for an order."""
    return f"Shipping info for order #{order_id}: Arriving tomorrow"

tools = [
    Tool(name="get_order_status", func=get_order_status, description="Get order status"),
    Tool(name="get_shipping_info", func=get_shipping_info, description="Get shipping info")
]

# Initialize agent
llm = OpenAI()
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Run query
result = agent.run("What's the status of my order #123?")
print(result)  # Output: Order #123: Shipped
```

### Resources
- [Guardrails AI Documentation](https://www.guardrailsai.com/docs)
- [Hugging Face Models](https://huggingface.co/models)
- [Tool Calling with LLMs](https://www.theregister.com/2024/08/26/ai_llm_tool_calling/)

### Industry Application
- **E-Commerce**: Build a customer support bot that retrieves order details and updates statuses via tool calls, integrating with a CRM system.

## Comparison of Tool Calling Approaches

| **Approach** | **Model Type** | **Advantages** | **Disadvantages** |
|--------------|----------------|----------------|-------------------|
| Native Tool Calling | Large (e.g., GPT-4) | Seamless integration, high accuracy | Higher cost, proprietary |
| Structured Output | Small (e.g., Mistral-7B) | Cost-effective, open-source | Requires manual parsing, less consistent |
| Agent-Based (LangChain) | Any | Flexible, supports multiple tools | Complex setup, potential latency |
| Griptape Orchestration | Any | Advanced workflow management | Steeper learning curve |

## Challenges and Best Practices

### Challenges
- **Consistency**: Small models may produce inconsistent tool call outputs, requiring robust validation.
- **Latency**: API calls can introduce delays, impacting real-time performance.
- **Security**: Unsanitized inputs or outputs can lead to injection attacks or data leaks.

### Best Practices
- **Validation**: Use Pydantic or Guardrails AI to validate tool call arguments.
- **Error Handling**: Implement retry mechanisms for failed tool calls or invalid outputs.
- **Testing**: Use real-world queries and data to ensure reliability in production.
- **Optimization**: Cache frequent API responses or batch requests to reduce latency.

## Staying Updated
- **Documentation**: Regularly check updates for LangChain, OpenAI, and Griptape, as Tool Calling features evolve rapidly.
- **Communities**: Engage with platforms like Reddit’s r/LocalLLLaMA or Hugging Face forums for insights on small models.
- **Articles**: Read recent posts on [Medium](https://medium.com) or [Analytics Vidhya](https://www.analyticsvidhya.com) for industry trends.

## Conclusion
Tool Calling is a cornerstone of LLM-driven applications, enabling seamless integration with external systems for tasks like data retrieval, automation, and real-time decision-making. While large models offer native support, small models can achieve similar functionality through structured output methods and libraries like LangChain, Griptape, and Instructor. By mastering the concepts, practices, and resources in this guide, you can build robust, industrial-grade applications that leverage Tool Calling for diverse use cases, from customer support to workflow automation. Experiment with various tools and stay updated with advancements to enhance your expertise as of August 6, 2025.

---

# Tool calling

#### **3. Tool Calling**

* **Goal**: Let the LLM decide when and how to call APIs/tools.
* **Key skills**:

  * Designing tool schemas
  * Passing intermediate results back to LLM
  * Handling failures & retries
* **Libraries**:

  * **OpenAI SDK** → `tools=[...]` parameter
  * **LangChain Agents** → `initialize_agent`
  * **LlamaIndex Tools** → `ToolMetadata`
* **Exercise**: Give an LLM a calculator and weather API as tools; make it answer “What’s the sum of the current temperature in Delhi and 100?”

## **Day 4 – Tool Calling**

**Focus:** Multiple functions, decision-making.
**Concepts:**

* Tools as callable APIs.
* When to call which tool.
* Returning intermediate results.

**Practice:**

* Give LLM calculator + weather API tools.
* Make it answer “What’s temp in Delhi + 100?”

**Resources:**

* [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
* [Griptape Docs](https://docs.griptape.ai/) 


### Day 4: Tool Calling
**Focus**: Allow LLMs to decide when and how to use external tools or APIs.

**Key Concepts**:
- **Tool Schemas**: Designing schemas for external tools.
- **Decision-Making**: Enabling LLMs to choose the right tool for a task.
- **Error Handling**: Managing tool call failures and retries.

**Practice**:
1. Provide the LLM with multiple tools (e.g., calculator, weather API).
2. Use LangChain’s `initialize_agent` to create an agent that selects tools based on user input.
3. Test with a query like “What’s the temperature in Delhi plus 100?”
4. Explore Griptape for advanced tool orchestration.

**Resources**:
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [Griptape Documentation](https://docs.griptape.ai/)
- [Tool Calling in LLMs](https://www.analyticsvidhya.com/blog/2024/08/tool-calling-in-llms/)

**Industry Application**:
- Create a customer support bot that fetches order details from a database.  
---
Perfect — Tool Calling is where your LLM systems start to feel like **real agents**. Here's a **compact and structured rewrite** of your **Tool Calling module**, keeping your focus areas in mind: comparison with function calling, chaining, real API integration, parallelism, and error handling.

---

## 🛠️ Module 3: Tool Calling

> **Goal:** Enable LLMs to dynamically select, call, and chain multiple tools (functions or APIs) during task execution — with real-world integration and reasoning.

---

### 🔄 Function Calling vs Tool Calling

| Feature            | **Function Calling**          | **Tool Calling**                          |
| ------------------ | ----------------------------- | ----------------------------------------- |
| Scope              | Usually 1 function per prompt | Multiple tools available per prompt       |
| Output             | Structured arguments          | Tool name + args + intermediate results   |
| Use Case           | Simple API wrappers           | Complex reasoning, multi-step workflows   |
| Parallel calls     | ❌ Typically not               | ✅ Supported (via agent framework)         |
| Reasoning required | Low                           | Medium to High (decide what/when to call) |

---

### 🔑 Key Concepts

* Defining tool metadata (name, input schema, description)
* Chaining tools for multi-hop reasoning
* Real API integrations (e.g., weather, calculator, DB)
* Handling failures & retries
* Parallel vs in-sequence tool use

---

### 🔁 4-Step Learning Path

#### ✅ **Step 1: LangChain Tool Agent**

* Define tools: calculator, weather API, search
* Use `initialize_agent()` with `AgentType.OPENAI_FUNCTIONS`
* Test: “What’s the temperature in Delhi plus 100?”

📦: `langchain`, `openai`, `requests`
🔗: [LangChain Agents](https://python.langchain.com/docs/modules/agents/)

---

#### ✅ **Step 2: Multi-Tool & Chained Calls**

* Add custom tools (e.g., `get_shipping_status(order_id)`)
* Use memory or intermediate results to chain tool outputs
* Test chained tasks:

  > “Find the current temp in Delhi, then give me a packing recommendation.”

📦: `langchain`, `pydantic`, `dotenv`
🔗: [Custom Tools in LangChain](https://python.langchain.com/docs/modules/agents/tools/custom_tools)

---

#### ✅ **Step 3: Custom Tool Calling with Local Models**

* Simulate tool calling by prompting local model (e.g. Mistral-7B) to return:

  ```json
  { "tool": "get_weather", "args": { "city": "Delhi" } }
  ```
* Parse manually and dispatch
* Use retry logic + structured fallback

📦: `transformers`, `json`, `re`, `tenacity`

---

#### ✅ **Step 4: Parallel / Dynamic Tool Calling**

* Add logic for:

  * Parallel tool calls
  * Conditional tool use
  * Error fallbacks
* Integrate real APIs (weather, finance, etc.)
* Optionally: Build a minimal **Tool Router**

📦: `asyncio`, `aiohttp`, `langchain`, `json`

---

### 💻 Exercises

* Query: “Get current weather in Mumbai and convert it to Fahrenheit”
* Tool Chain: `get_weather` → `unit_converter`
* Use both OpenAI + local model to simulate tool use
* Add retry/error handler when API fails

---

### 💼 Real-World Applications

* Customer support bot → fetch order, track shipment, suggest help docs
* Dev assistant → run code, search docs, return summaries
* Internal automation → read from DB, validate, then call downstream API

---

Let me know when you're ready for **Module 4: Reasoning**, and I’ll keep it just as compact and progressive.
