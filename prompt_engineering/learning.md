A prompt is the input you give to a language model (like ChatGPT, Claude, Gemini) to instruct it to produce a specific output. 
Prompts are written in natural language and guide the behavior, tone, style, and content of the model's response.
Prompts are like programming instructions written in plain English. You're giving the model a command set to interpret.

Prompting is the process of providing input to a model. The quality of your output often depends on how well you're able to prompt the model.
Prompt Engineering is the iterative process of developing a prompt by modifying or changing the prompting technique that you are using.


LLMs transform prompts into tokens, then process them using embeddings and attention.
Tokenization:
Words → Tokens → Vectors
Example: "ChatGPT is great" → ["Chat", "G", "PT", "is", "great"]
Embeddings:
Tokens are mapped into high-dimensional vectors capturing meaning.


Crafting effective prompts requires careful consideration of several key aspects:

Clarity: Prompts should be clear, concise, and easy to understand, avoiding ambiguity and jargon.

Context: Providing adequate context is crucial for guiding the model towards the desired outcome. This includes background information, relevant examples, and specific details.

Examples: Including examples of the desired output can help the model better understand expectations and generate more relevant responses.

Keywords: Using keywords can help steer the model’s attention towards specific concepts or topics.

Tone: The tone of the prompt can influence the style and formality of the model’s response. A playful manner encourages creativity, while a formal way promotes factual accuracy.

Markdown headers and lists can be helpful to mark distinct sections of a prompt, and to communicate hierarchy to the model. They can also potentially make your prompts more readable during development. XML tags can help delineate where one piece of content (like a supporting document used for reference) begins and ends. XML attributes can also be used to define metadata about content in the prompt that can be referenced by your instructions.

Models can only handle so much data within the context they consider during a generation request. This memory limit is called a *context window*, which is defined in terms of tokens (chunks of data you pass in, from text to images).


--Optimizing Performance For reasoning   
Temperature and Token Management  
The model performs best with temperature settings between 0.5-0.7, with lower values (closer to 0.5) producing more consistent mathematical proofs and higher values allowing for more creative problem-solving approaches. Monitor and adjust your token usage based on the complexity of your reasoning tasks - while the default max_completion_tokens is 1024, complex proofs may require higher limits.

Prompt Engineering
To ensure accurate, step-by-step reasoning while maintaining high performance:

DeepSeek-R1 works best when all instructions are included directly in user messages rather than system prompts.
Structure your prompts to request explicit validation steps and intermediate calculations.
Avoid few-shot prompting and go for zero-shot prompting only.


Generative AI (GenAI) refers to Artificial Intelligence that can be used to create new content such as articles or images, which previously only humans could do. In short, GenAI can create stuff. GenAI is expected to significantly change the way we work and live