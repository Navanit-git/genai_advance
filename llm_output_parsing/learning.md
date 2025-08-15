Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema, so you don't need to worry about the model omitting a required key, or hallucinating an invalid enum value.


If you are connecting the model to tools, functions, data, etc. in your system, then you should use function calling
If you want to structure the model's output when it responds to the user, then you should use a structured response_format


Step 1: Define your object
First you must define an object or data structure to represent the JSON Schema that the model should be constrained to follow. See the examples at the top of this guide for reference.
To maximize the quality of model generations, we recommend the following:
Name keys clearly and intuitively
Create clear titles and descriptions for important keys in your structure
Create and use evals to determine the structure that works best for your use case


Pydantic is a widely-used data validation and conversion library. It relies heavily on Python type declarations. Pydantic supports converting Pydantic classes into JSON-serialized schema objects which conform to popular standards. 