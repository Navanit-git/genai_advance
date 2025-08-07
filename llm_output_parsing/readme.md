# LLM Output Methods Study Plan

## Introduction

 A comprehensive guide designed to help you master four critical techniques for working with Large Language Models (LLMs): **Structured Output**, **Function Calling**, **Tool Calling**, and **Reasoning**. These methods enable LLMs to produce machine-readable outputs, interact with external systems, and solve complex problems, making them essential for building robust, industrial-grade AI applications.

## Purpose

The goal is to provide a clear, modular study plan to:

- Understand and implement **Structured Output** to ensure consistent, machine-readable LLM responses (e.g., JSON, XML, CSV).
- Master **Function Calling** to enable LLMs to invoke predefined functions with structured arguments.
- Leverage **Tool Calling** to integrate LLMs with external tools or APIs for dynamic tasks.
- Apply **Reasoning** techniques like Chain-of-Thought (CoT), self-consistency, and Tree of Thoughts to solve complex problems.
- Combine these methods to build sophisticated AI systems, such as logistics planners, chatbots, or decision-support tools.



# Structured Output  

**Focus**: Learn to prompt LLMs to produce predictable formats (JSON, XML, CSV, YAML) for integration with automated systems.

#### **Step 1: OpenAI + Pydantic**
* Use `response_format="json"` with OpenAI API.
* Define a Pydantic model (e.g. `Person(name: str, age: int)`).
* Parse & validate response. Retry on failure.  
#### **Step 2: LangChain Structured Output**
* Use `StructuredOutputParser` with a Pydantic schema.
* Prompt LLM for structured formats like job listings or product specs.
#### **Step 3: LlamaIndex Schema Extraction**
* Define schema → Use `StructuredExtractor` or `SchemaExtractionEngine`.
* Extract structured info from semi-structured docs (e.g., resumes, invoices).
#### **Step 4: Custom Extraction Pipeline**
* Prompt for JSON/YAML manually.
* Parse with `json.loads()` or regex.
* Add retry/fix logic (e.g., `fix_json`, `tenacity`).


---

# 2: Function Calling

**Focus**: Enable LLMs to invoke predefined functions by generating structured arguments, supporting both large and small models.  
### Key Concepts

* Function schema definition (`name`, `parameters`, `types`)
* Mapping LLM output to executable functions
* Error handling, retries, and local model workarounds
* Multi-function and dynamic calling flows  



#### **Step 1: OpenAI Function Calling (Built-In)**

* Define `get_weather(city: str, date: str)`
* Use `tools=[{type: "function", function: {...}}]`
* Parse LLM response → auto-call function with extracted args  
📦: `openai`
🔗: [Function Calling Docs](https://platform.openai.com/docs/guides/function-calling)



#### **Step 2: LangChain Function Calling**

* Wrap the same function inside `Tool` or `OpenAIFunctionsAgent`
* Let LangChain handle argument extraction and tool routing
* Add multiple tools (e.g., `search_tool`, `calculator`)  
📦: `langchain`
🔗: [LangChain Function Calling](https://python.langchain.com/docs/modules/agents/tools/function_calling/)

#### **Step 3: Custom Function Calling with Local Models**

* Simulate function calling using LLM + regex/JSON parsing
* Prompt local model.
* Parse manually and route to Python function  
📦: `transformers`, `json`, `re`  
🔗: Any Mistral-based inference setup (e.g., `vllm`, `ollama`, `LM Studio`)

#### **Step 4: Advanced / Multi-Function Calling**

* Define multiple callable functions in a registry
* Prompt LLM to choose correct one and provide args
* Handle unknown, dynamic, or user-defined functions
* Optional: Support nested or chained function calls

--- 

# 3: Tool Calling

- **Focus**: Enable LLMs to dynamically select, call, and chain multiple tools (functions or APIs) during task execution — with real-world integration. 
- **Key Concepts**:
  - Designing tool schemas for diverse applications.
  - Chaining tools for multi-step tasks.
  - Implementing tool calling with small models via structured outputs.  
  - Real API integrations (e.g., weather, calculator, DB)
 - Handling failures & retries
 - Parallel vs in-sequence tool use
### Learning Path

#### **Step 1: LangChain Tool **

* Define tools: calculator, weather API, search
* Test: “What’s the temperature in Delhi plus 100?”  
📦: `langchain`, `openai`, `requests`
🔗: [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
####  **Step 2: Multi-Tool & Chained Calls**  

* Add custom tools (e.g., `get_shipping_status(order_id)`)
* Use memory or intermediate results to chain tool outputs
* Test chained tasks:

  > “Find the current temp in Delhi, then give me a packing recommendation.”
  
  📦: `langchain`, `pydantic`, `dotenv`  
  🔗: [Custom Tools in LangChain](https://python.langchain.com/docs/modules/agents/tools/custom_tools)

#### **Step 3: Custom Tool Calling with Local Models**

* Simulate tool calling by prompting local model (e.g. Mistral-7B) to return:

  ```json
  { "tool": "get_weather", "args": { "city": "Delhi" } }
  ```
* Parse manually and dispatch
* Use retry logic + structured fallback  
📦: `transformers`, `json`, `re`, `tenacity`

#### **Step 4: Parallel / Dynamic Tool Calling**
* Add logic for:

  * Parallel tool calls
  * Conditional tool use
  * Error fallbacks
* Integrate real APIs (Email, websearch, file reader.)
* Optionally: Build a minimal **Tool Router**

📦: `asyncio`, `aiohttp`, `langchain`, `json`

# Module 4: Reasoning  

**Goal:** Train LLMs to think step-by-step using prompt engineering and advanced “thinking” models. Learn to extract intermediate reasoning and final answers separately.

### 🧩 Two Reasoning Styles

| Method                     | Description                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------ |
| **Prompt-based Reasoning** | Use Chain-of-Thought (CoT), self-consistency, ToT                                    |
| **Reasoning LLMs**         | Use models with built-in reasoning capabilities (e.g., Claude 3.5 Sonnet, GPT o1/o3) |



### 🔑 Key Concepts

* CoT prompting: “Let’s think step by step…”
* Self-consistency: Sample multiple reasoning paths, choose best
* Tree/Graph of Thoughts: Parallel exploration of reasoning
* Separating **reason** and **answer** (e.g., `"thought": "...", "answer": "..."`)

---

### Learning Path

#### **Step 1: Prompt-based Reasoning (Manual)**

* Use CoT Prompt 
* Ask the same question multiple times (e.g., 5–10 generations).
* Collect multiple reasoning paths and pick the most frequent answer. 
* Use parsing method to parse the thinking and actual answer. 

#### **Step 2: Reasoning Models (Built-In Thinking)**

* Use Claude 3.5 Sonnet or GPT o1/o3 (reasoning-optimized).
* Enable “thinking” mode if available (Claude’s default behavior).
* Use parsing method to parse these. 

#### **Step 3: Tree/Graph of Thoughts (Advanced Planning)**

* Use DSPy or custom code to explore multiple reasoning paths.  
🔗: [DSPy GitHub](https://github.com/stanfordnlp/dspy)
---





