# Structured Output Methods for LLMs: A Comprehensive Guide for Industrial Applications

## Introduction
Structured output methods are critical for transforming their natural language responses into machine-readable formats like JSON, XML, CSV, and YAML. 

## Module 1: Basics of Structured Output

### Concepts

- **Supported Formats**:
  - **JSON**: Widely used for its simplicity and compatibility with programming languages like Python.
  - **XML**: Suitable for hierarchical data, common in enterprise systems and legacy applications.
  - **CSV**: Ideal for tabular data, often used in data analysis and reporting.
  - **YAML**: Human-readable and used in configuration files or data serialization.
  - **Other Formats**: Protocol Buffers for high-performance applications or custom formats for niche use cases.
  
- **Schema Validation**:
  - Ensures outputs conform to predefined structures, preventing errors in downstream systems.
  - Tools like Pydantic validate data and convert it into Python objects for easy manipulation.
- **Prompt Engineering**:
  - Crafting prompts to instruct LLMs to return specific formats, though this alone may not guarantee valid outputs.

### Practice
1. **Setup**: Install Python and required libraries: `pip install openai pydantic`.
2. **JSON Output with OpenAI SDK**: Use `response_format={"type": "json_object"}` to request JSON outputs.
   - Example Prompt: “Return a JSON object with name and age for a person.”
3. **Schema Definition**: Create a Pydantic model to define the expected structure (e.g., `{ "name": str, "age": int }`).
4. **Validation and Retry**: Validate the LLM’s response with Pydantic and implement retry logic for invalid outputs.
5. **Experiment with Other Formats**: Modify the prompt to request XML or CSV and parse the output manually or with libraries like `xml.etree.ElementTree` or `csv`.

### Example: JSON Output with Validation
```python
import openai
from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    name: str
    age: int

prompt = "Return a JSON object with name and age for a person."
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"}
)
data = response.choices[0].message.content
try:
    person = Person.model_validate_json(data)
    print(person)
except ValidationError:
    print("Invalid output, retrying...")
    # Retry logic: Re-prompt or adjust the input
```

### Example: XML Output
```python
import openai
import xml.etree.ElementTree as ET

prompt = "Return an XML object with name and age for a person, e.g., <person><name>John</name><age>30</age></person>."
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)
xml_data = response.choices[0].message.content
try:
    root = ET.fromstring(xml_data)
    name = root.find("name").text
    age = int(root.find("age").text)
    print(f"Name: {name}, Age: {age}")
except ET.ParseError:
    print("Invalid XML, retrying...")
```

### Resources
- [OpenAI Structured Outputs Documentation](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Guardrails AI](https://www.guardrailsai.com/) for schema enforcement.

### Industry Application
- **Data Extraction**: Extract structured data (e.g., customer details) from feedback forms for database storage.
- **Example**: Parse unstructured survey responses into JSON for CRM integration.

## Module 2: Structured Output with Libraries

### Concepts
- **Key Libraries**:
  - **LangChain**: Provides `StructuredOutputParser` and `PydanticOutputParser` for parsing LLM outputs into structured formats like JSON, XML, or CSV.
  - **Instructor**: Simplifies typed output mapping by integrating with Pydantic for schema validation.
  - **Guardrails AI**: Enforces schema compliance and automatically re-prompts the LLM if outputs fail validation.
- **Schema Definition**:
  - Use Pydantic to define complex data models with nested structures or type constraints.
- **Auto-Parsing**:
  - Automatically convert LLM outputs into structured formats, reducing manual processing.
- **Error Handling**:
  - Implement mechanisms to handle invalid outputs, such as retries or fallback prompts.

### Practice
1. **LangChain Setup**: Install `langchain` and configure with an LLM provider (e.g., OpenAI).
2. **StructuredOutputParser**: Use LangChain to parse outputs into JSON or other formats.
3. **Instructor**: Experiment with Instructor for typed output mapping.
4. **Guardrails AI**: Implement schema enforcement and retry logic for robust outputs.
5. **Test Case**: Prompt the LLM to extract product details from a description and validate the output.

### Example: LangChain with StructuredOutputParser
```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI

response_schemas = [
    ResponseSchema(name="name", description="The person's name", type="string"),
    ResponseSchema(name="age", description="The person's age", type="integer")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template(
            "Format the person's information as JSON\n{format_instructions}\nPerson: {person}"
        )
    ],
    input_variables=["person"],
    partial_variables={"format_instructions": format_instructions}
)

chain = prompt | OpenAI() | output_parser
result = chain.invoke({"person": "John Doe, 30 years old"})
print(result)  # Output: {'name': 'John Doe', 'age': 30}
```

### Example: CSV Output with LangChain
```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate
from langchain.llms import OpenAI
import csv
import io

response_schemas = [
    ResponseSchema(name="name", description="The person's name", type="string"),
    ResponseSchema(name="age", description="The person's age", type="integer")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

prompt = ChatPromptTemplate.from_template(
    "Return a CSV with name and age for a person\n{format_instructions}\nPerson: {person}"
)

chain = prompt | OpenAI() | output_parser
result = chain.invoke({"person": "John Doe, 30 years old"})

# Convert to CSV
output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["name", "age"])
writer.writeheader()
writer.writerow(result)
print(output.getvalue())
```

### Resources
- [LangChain Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers)
- [Instructor GitHub](https://github.com/jxnl/instructor)
- [Guardrails AI Documentation](https://www.guardrailsai.com/docs)
- [Mastering Structured Output in LLMs](https://medium.com/@docherty/mastering-structured-output-in-llms-choosing-the-right-model-for-json-output-with-langchain-be29fb6f6675)

### Industry Application
- **Invoice Processing**: Extract structured data (e.g., item names, prices) from invoices for accounting systems.
- **Example**: Parse invoice text into JSON or CSV for integration with financial software.

## Module 3: Advanced Techniques for Structured Output

### Concepts
- **Constrained Decoding**:
  - Modifies the LLM’s output generation process to enforce specific formats by adjusting logits.
  - Ensures strict adherence to schemas, reducing the need for post-processing.
- **Function Calling for Structured Output**:
  - LLMs can invoke predefined functions that return structured data, supported by models like GPT-4o.
  - Useful for integrating structured outputs with external systems.
- **Multi-Step Structured Output**:
  - Breaks complex tasks into sequential steps, each producing structured output.
  - Enhances reliability for workflows requiring multiple data transformations.

### Practice
1. **Constrained Decoding**: Experiment with libraries like `tiktoken` or custom implementations to enforce JSON or XML formats.
2. **Function Calling**: Use OpenAI’s function calling API to generate structured outputs.
3. **Multi-Step Pipeline**: Build a pipeline that processes unstructured text through multiple steps, each producing structured output.
4. **Test Case**: Extract weather data from a user query and format it into JSON or XML.

### Example: Function Calling for Structured Output
```python
import openai
from pydantic import BaseModel

class Weather(BaseModel):
    city: str
    temperature: float
    condition: str

functions = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a given city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The city to get weather for"},
            },
            "required": ["city"]
        }
    }
]

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in New York?"}],
    functions=functions,
    function_call="auto"
)
function_call = response.choices[0].message.function_call
if function_call:
    # Simulate API call and return structured output
    weather_data = {"city": "New York", "temperature": 20.5, "condition": "Sunny"}
    weather = Weather(**weather_data)
    print(weather)
```

### Example: Multi-Step Pipeline
```python
from langchain.llms import OpenAI
from langchain.chains import SequentialChain, LLMChain
from langchain.prompts import PromptTemplate
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

# Step 1: Extract raw data
extract_prompt = PromptTemplate(
    input_variables=["text"],
    template="Extract product name and price from: {text}"
)
extract_chain = LLMChain(llm=OpenAI(), prompt=extract_prompt, output_key="raw_data")

# Step 2: Format into JSON
format_prompt = PromptTemplate(
    input_variables=["raw_data"],
    template="Format this data into JSON: {raw_data}"
)
format_chain = LLMChain(llm=OpenAI(), prompt=format_prompt, output_key="json_data")

# Combine into a pipeline
pipeline = SequentialChain(
    chains=[extract_chain, format_chain],
    input_variables=["text"],
    output_variables=["json_data"]
)

result = pipeline({"text": "iPhone 15 Pro, $999"})
print(result["json_data"])
```

### Resources
- [Structured Output Generation in LLMs](https://medium.com/@emrekaratas-ai/structured-output-generation-in-llms-json-schema-and-grammar-based-decoding-6a5c58b698a6)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)

### Industry Application
- **API-Driven Workflows**: Use function calling to fetch and format data from external APIs into structured outputs.
- **Example**: Retrieve stock prices and format them into JSON for a financial dashboard.

## Module 4: Industrial Applications of Structured Output

### Concepts
- **Real-World Use Cases**:
  - **Data Extraction**: Parse unstructured text (e.g., emails, reports) into structured formats for analysis or storage.
  - **API Integration**: Format LLM outputs to interact with external APIs, such as weather or payment services.
  - **Workflow Automation**: Use structured outputs to drive multi-step processes in business applications.
  - **Intelligent Agents**: Build agents that produce structured responses for database queries or user interactions.
- **Challenges**:
  - **Consistency**: LLMs may produce invalid or incomplete outputs, requiring robust validation.
  - **Scalability**: Handling large volumes of data or frequent API calls can introduce latency.
  - **Error Handling**: Managing edge cases like malformed outputs or API failures.
- **Best Practices**:
  - Use validation libraries like Pydantic or Guardrails AI to enforce schemas.
  - Implement retry mechanisms for failed outputs.
  - Test with real-world data to ensure robustness in production.

### Practice
1. **Project: Product Data Extraction**:
   - **Input**: Unstructured product description (e.g., “iPhone 15 Pro, $999, Smartphone”).
   - **Output**: Structured JSON or CSV with fields like `name`, `price`, `category`.
   - **Tools**: Use LangChain’s `StructuredOutputParser` or Guardrails AI for schema enforcement.
2. **Project: API Integration**:
   - Fetch data from a public API (e.g., weather API) and format it into JSON or XML.
   - Use Pydantic to validate the output structure.
3. **Test Case**: Process a batch of product descriptions and store the results in a database.

### Example: Product Data Extraction Project
```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate
from langchain.llms import OpenAI

response_schemas = [
    ResponseSchema(name="name", description="Product name", type="string"),
    ResponseSchema(name="price", description="Product price", type="float"),
    ResponseSchema(name="category", description="Product category", type="string")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

prompt = ChatPromptTemplate.from_template(
    "Extract product details from: {description}\n{format_instructions}"
)

chain = prompt | OpenAI() | output_parser
result = chain.invoke({"description": "iPhone 15 Pro, $999, Smartphone"})
print(result)  # Output: {'name': 'iPhone 15 Pro', 'price': 999.0, 'category': 'Smartphone'}
```

### Resources
- [Structured Outputs in LLMs](https://www.leewayhertz.com/structured-outputs-in-llms/)
- [Parsing LLM Structured Outputs in LangChain](https://medium.com/@juanc.olamendy/parsing-llm-structured-outputs-in-langchain-a-comprehensive-guide-f05ffa88261f)

### Industry Application
- **Supply Chain Management**: Extract structured data from supplier emails to update inventory databases.
- **Example**: Parse email content into JSON with fields like `item`, `quantity`, and `delivery_date`.

## Comparison of Structured Output Formats

| **Format** | **Use Case** | **Advantages** | **Disadvantages** |
|------------|--------------|----------------|-------------------|
| JSON       | API integration, data serialization | Simple, widely supported, easy to parse | Limited for complex hierarchical data |
| XML        | Enterprise systems, hierarchical data | Supports complex structures, widely used in legacy systems | Verbose, harder to read |
| CSV        | Tabular data, reporting | Simple, compact, easy to process | Limited to flat data, no nesting |
| YAML       | Configuration files, human-readable data | Easy to read, supports nesting | Less common in API contexts |
| Protocol Buffers | High-performance applications | Compact, fast, strongly typed | Requires additional setup, less human-readable |

## Challenges and Considerations
- **Consistency**: LLMs may not always produce valid structured outputs, especially with complex schemas.
- **Error Handling**: Implement robust validation and retry mechanisms to handle malformed outputs.
- **Performance**: Generating structured outputs can be slower than unstructured text, especially with constrained decoding.
- **Scalability**: Optimize for large-scale data processing by caching frequent outputs or batching requests.

## Best Practices
- **Validation**: Use Pydantic or Guardrails AI to enforce schemas and catch errors early.
- **Retries**: Implement retry logic for invalid outputs, adjusting prompts as needed.
- **Testing**: Use real-world data to test outputs for accuracy and reliability.
- **Format Selection**: Choose the format based on the use case (e.g., JSON for APIs, CSV for reports).

## Staying Updated
- **Documentation**: Regularly check updates for LangChain, OpenAI, and Pydantic, as features evolve rapidly.
- **Communities**: Engage with platforms like Reddit’s r/MachineLearning or LangChain’s Discord for the latest insights.
- **Articles**: Read recent posts on [Medium](https://medium.com) or [LeewayHertz](https://www.leewayhertz.com) for industry trends.

## Conclusion
Structured output methods are a cornerstone of leveraging LLMs in industrial applications, enabling reliable integration with backend systems and automation workflows. By mastering the basics, utilizing libraries like LangChain and Pydantic, exploring advanced techniques like constrained decoding, and applying these skills to real-world projects, you can build robust, production-ready solutions. This modular guide provides a clear path to achieving proficiency in structured output methods, preparing you for advanced backend development as of August 6, 2025.

---  
# Structure Output

## **Structured Output Basics**

**Focus:** Get LLMs to output predictable JSON/XML.
**Concepts:**

* Why unstructured text is unreliable for automation.
* Prompting for JSON.
* Schema validation.

**Practice:**

* Use **OpenAI SDK** with `response_format={"type": "json_object"}`.
* Validate with **Pydantic**.
* Retry if schema invalid.

**Resources:**

* [OpenAI JSON mode docs](https://platform.openai.com/docs/guides/text-generation/json-mode)
* [Guardrails AI](https://www.guardrailsai.com/)

## **Day 2 – Structured Output with Libraries**

**Focus:** Schema-enforced responses.
**Concepts:**

* Defining schema with Pydantic.
* Auto-parsing output.
* Handling invalid model output.

**Practice:**

* **LangChain** → `StructuredOutputParser`
* **Instructor** → Typed function call mapping

**Resources:**

* [LangChain Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers)
* [Instructor GitHub](https://github.com/jxnl/instructor)

#### **1. Structured Output**

* **Goal**: Make LLMs return predictable formats like JSON, XML, or specific schemas.
* **Key skills**:
  * Prompt engineering for deterministic formats
  * Schema validation
  * Automatic retries & parsing errors
* **Libraries**:

  * **OpenAI SDK** → `response_format={"type": "json_object"}` (simple)
  * **LangChain** → `PydanticOutputParser`, `StructuredOutputParser`
  * **LlamaIndex** → `SchemaExtraction` tools
  * **Guardrails AI** → enforce JSON schemas at runtime
* **Exercise**: Build a prompt that always returns a list of objects `{ "name": string, "age": int }` and validate it with Pydantic.


### Day 1: Structured Output Basics
**Focus**: Learn to prompt LLMs to produce structured outputs like JSON or XML, essential for integrating with automated systems.

**Key Concepts**:
- **Unstructured vs. Structured Output**: Unstructured text is unreliable for automation due to variability; structured outputs ensure consistency and machine-readability.
- **Prompting for Structure**: Crafting prompts to instruct LLMs to return specific formats.
- **Schema Validation**: Using tools to validate output adherence to predefined schemas.

**Practice**:
1. Install Python and libraries: `pip install openai pydantic`.
2. Use OpenAI SDK to request JSON outputs with `response_format={"type": "json_object"}`.
   - Example: Prompt the LLM with “Return a JSON object with name and age for a person.”
3. Define a Pydantic model to represent the expected output structure (e.g., `{ "name": str, "age": int }`).
4. Validate the LLM’s response against the Pydantic model.
5. Implement retry logic to re-prompt the LLM if the output fails validation.

**Resources**:
- [OpenAI Structured Outputs Documentation](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Guardrails AI](https://www.guardrailsai.com/) for schema enforcement.

**Industry Application**:
- Extract structured data from customer feedback forms for database storage.

### Day 2: Structured Output with Libraries
**Focus**: Leverage libraries to enforce and validate structured   outputs, ensuring reliability in production.

**Key Concepts**:
- **Schema Definition**: Using Pydantic to define complex data models.
- **Auto-Parsing**: Automatically parsing LLM outputs into structured formats.
- **Error Handling**: Managing invalid outputs through retries or re-prompting.

**Practice**:
1. Use LangChain’s `StructuredOutputParser` to parse LLM outputs into JSON.
2. Experiment with Instructor to map outputs to Pydantic models.
3. Implement Guardrails AI to enforce schema compliance and handle validation failures.
4. Test with a prompt like “Extract product details from this description” and validate the output.

**Resources**:
- [LangChain Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers)
- [Instructor GitHub](https://github.com/jxnl/instructor)
- [Guardrails AI Documentation](https://www.guardrailsai.com/docs)
- [Mastering Structured Output in LLMs](https://medium.com/@docherty/mastering-structured-output-in-llms-choosing-the-right-model-for-json-output-with-langchain-be29fb6f6675)

**Industry Application**:
- Automate extraction of structured data from invoices for accounting systems.  
--- 


Great direction — you're setting a solid foundation by breaking **structured output** into 4 progressive steps, each adding abstraction or control. I’ll now rewrite your section in a professional, clean README-style structure with clear milestones for each of the four phases:

---

## ✅ 1: Structured Output

> **Objective:** Learn how to get predictable, schema-validated structured outputs (like JSON/XML) from LLMs using different methods and libraries. This is critical for building reliable pipelines, agents, and automated systems.

---

### 🧠 Core Concepts

* Difference between unstructured vs. structured output in LLMs.
* How prompt design influences formatting (e.g., JSON vs. XML).
* Schema validation using `pydantic`.
* Retry logic and validation feedback loops.
* Comparison of OpenAI-native, LangChain, LlamaIndex, and custom pipelines.

---

## 🔁 Learning Steps

---

### 🔹 **Step 1: Native OpenAI + Pydantic**

> Use OpenAI's `response_format="json"` and validate the output manually with Pydantic.

#### ✅ Tasks:

* Prompt OpenAI to return a person profile:

  ```json
  { "name": "Alice", "age": 30, "email": "alice@example.com" }
  ```
* Use `response_format="json"` in the API call.
* Define a matching `pydantic.BaseModel` schema.
* Handle invalid outputs with try/catch + retry logic.

#### 🛠 Tech Stack:

* `openai`
* `pydantic`

#### 📘 Resources:

* [OpenAI JSON mode docs](https://platform.openai.com/docs/guides/text-generation/json-mode)
* [Pydantic docs](https://docs.pydantic.dev/latest/)

---

### 🔹 **Step 2: Using LangChain Structured Output Parser**

> Let LangChain auto-parse and validate LLM output using prompt templates + parsers.

#### ✅ Tasks:

* Use `StructuredOutputParser` with a `Pydantic` model.
* Prompt the LLM to generate output for a **job listing** schema.
* Parse, validate, and handle parsing errors automatically.

#### 🛠 Tech Stack:

* `langchain`
* `pydantic`
* `OpenAI`

#### 📘 Resources:

* [LangChain Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)
* LangChain Cookbook on GitHub

---

### 🔹 **Step 3: Using LlamaIndex Structured Extraction**

> Use LlamaIndex’s high-level interface to extract structured info from unstructured text.

#### ✅ Tasks:

* Feed in sample documents (e.g., resume, invoice, or email).
* Define an `output_schema` using `pydantic`.
* Use `StructuredExtractor` or `SchemaExtractionEngine` to extract info into schema.
* Run evaluations on extraction quality.

#### 🛠 Tech Stack:

* `llama-index`
* `pydantic`

#### 📘 Resources:

* [LlamaIndex Structured Extraction Docs](https://docs.llamaindex.ai/en/stable/examples/structured/structured_output/)

---

### 🔹 **Step 4: Manual (Custom) Structured Output Extraction**

> Build your own lightweight structured output handler using regex, JSON parsing, and custom error handlers.

#### ✅ Tasks:

* Prompt for JSON or YAML manually from the LLM.
* Use `json.loads` and handle formatting edge cases.
* Add retry logic if format is invalid (e.g., try `fix_json` strategies).
* Compare performance with LangChain/LlamaIndex.

#### 🛠 Tech Stack:

* `json`
* `re` or `yaml`
* Optional: `tenacity` for retry logic

#### 📘 Resources:

* [Fix JSON from LLMs (blog)](https://dust.tt/blog/recovering-broken-json-llms/)
* Open-source utilities like `jsonfix` or your own fallback correction logic

---

## 🎯 Exercises (Cross-Cutting)

* Extract JSON from natural language description:

  > “A 34-year-old named Sarah works as a UX designer in Berlin. Her email is [sarah@example.com](mailto:sarah@example.com).”

  Extract:

  ```json
  {
    "name": "Sarah",
    "age": 34,
    "job_title": "UX designer",
    "city": "Berlin",
    "email": "sarah@example.com"
  }
  ```
* Try the same task across **all four steps** to compare reliability, ease of use, and performance.
* Bonus: Try generating **CSV** or **YAML** formats and parse them into Python objects.

---

## 💼 Industry Use Cases

* Invoice, receipt, or resume parsing into structured format.
* Auto-tagging customer support tickets with category and sentiment.
* Pulling structured insights from sales or meeting transcripts.

---

Would you like me to generate:

* 📁 A **starter folder structure** for these four stages, or
* ⚙️ A **working Jupyter notebook** template that covers the whole pipeline?



Absolutely — here’s a **more compact version** of the Structured Output module, while keeping clarity and actionability intact. Ideal for fitting into a multi-module README:

---

## 🧩 Module 1: Structured Output

> **Goal:** Make LLMs return predictable, schema-validated structured formats like JSON, CSV, or XML.

---

### 🔑 Key Concepts

* Prompting for structured formats (JSON, YAML, XML).
* Schema validation using `pydantic`.
* Handling invalid/malformed output.
* Comparing raw vs library-assisted parsing.

---

### 🔁 4-Step Learning Path

#### ✅ **Step 1: OpenAI + Pydantic**

* Use `response_format="json"` with OpenAI API.
* Define a Pydantic model (e.g. `Person(name: str, age: int)`).
* Parse & validate response. Retry on failure.

📦: `openai`, `pydantic`
🔗: [OpenAI JSON Mode](https://platform.openai.com/docs/guides/text-generation/json-mode)

---

#### ✅ **Step 2: LangChain Structured Output**

* Use `StructuredOutputParser` with a Pydantic schema.
* Prompt LLM for structured formats like job listings or product specs.

📦: `langchain`, `pydantic`
🔗: [LangChain Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers)

---

#### ✅ **Step 3: LlamaIndex Schema Extraction**

* Define schema → Use `StructuredExtractor` or `SchemaExtractionEngine`.
* Extract structured info from semi-structured docs (e.g., resumes, invoices).

📦: `llama-index`, `pydantic`
🔗: [LlamaIndex Structured Output](https://docs.llamaindex.ai/en/stable/examples/structured/structured_output/)

---

#### ✅ **Step 4: Custom Extraction Pipeline**

* Prompt for JSON/YAML manually.
* Parse with `json.loads()` or regex.
* Add retry/fix logic (e.g., `fix_json`, `tenacity`).

📦: `json`, `re`, `yaml`, `tenacity`

---

### 💻 Exercises

* Prompt to extract:

  ```json
  { "name": "Alice", "age": 30, "email": "alice@example.com" }
  ```
* Repeat across all 4 steps.
* Bonus: Output in CSV/XML and parse.

---

### 💼 Real-World Uses

* Invoice/receipt parsing → DB.
* Customer feedback → sentiment + tags.
* Resume parsing → HR systems.

---

Let me know when you're ready to move to **Module 2: Function Calling** and I’ll compact it in the same format.
