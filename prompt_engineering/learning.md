
Generative AI (GenAI) refers to Artificial Intelligence that can be used to create new content such as articles or images, which previously only humans could do. In short, GenAI can create stuff. GenAI is expected to significantly change the way we work and live

A prompt is the input you give to a language model (like ChatGPT, Claude, Gemini) to instruct it to produce a specific output. 
Prompts are written in natural language and guide the behavior, tone, style, and content of the model's response.
Prompts are like programming instructions written in plain English. You're giving the model a command set to interpret.
A prompt contains any of the following elements:
Instruction - a specific task or instruction you want the model to perform
Context - external information or additional context that can steer the model to better responses
Input Data - the input or question that we are interested to find a response for
Output Indicator - the type or format of the output.


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

Another common tip when designing prompts is to avoid saying what not to do but say what to do instead. This encourages more specificity and focuses on the details that lead to good responses from the model.

Models can only handle so much data within the context they consider during a generation request. This memory limit is called a *context window*, which is defined in terms of tokens (chunks of data you pass in, from text to images).


--Optimizing Performance For reasoning   
Temperature and Token Management  
The model performs best with temperature settings between 0.5-0.7, with lower values (closer to 0.5) producing more consistent mathematical proofs and higher values allowing for more creative problem-solving approaches. Monitor and adjust your token usage based on the complexity of your reasoning tasks - while the default max_completion_tokens is 1024, complex proofs may require higher limits.

Instruction Prompting

Role Prompting

Shot-Based Prompting
Zero-shot prompting: Use this when the task is simple, well-understood, or frequently encountered in the model's training data. It's efficient for tasks like basic arithmetic, general queries, or sentiment classification for common phrases.

One-shot prompting: This is helpful for tasks that need more specific guidance or when the model struggles with ambiguity. Providing a single example can clarify the task, improving accuracy in tasks like basic classification or structured information extraction.

Few-shot prompting: Best used for complex tasks requiring multiple examples to establish patterns. This technique is ideal for tasks that involve varied inputs, require precise formatting, or demand a higher degree of accuracy, such as generating structured outputs or handling nuanced classifications.

Priming chatbots (also known as prompt priming or inception prompts) is a powerful technique used to guide a chatbot's behavior in a desired direction. By framing or structuring the initial prompt, you can influence how the AI interprets user input and tailor its responses to fit specific objectives.


Self-Ask method
Self-Consistency

Memory-of-Thought (MoT) Prompting


Prompt Mining is a technique used to identify the best prompt template for a given [relation] between [subject] and [object] from a corpus of text. Similar to traditional mining, where you search for valuable resources, in prompt mining you use algorithms to uncover the prompt template giving the most accurate results.

The key point here is that Prompt Mining isn’t about selecting the best template for any general task. Instead, it’s focused on improving how Large Language Models (LLMs) retrieve factual knowledge. Essentially, it boosts accuracy by discovering the language patterns and templates the model has "learned" best during training. The goal is to find prompts that consistently trigger the model to predict correct factual information.

A prompt template is a structured format for presenting questions or statements to the model, often with placeholders for customization.



Universal Self-Consistency is a prompting technique used to refine and improve the accuracy of answers generated by a Large Language Model (LLM). It compiles multiple responses the model has previously given and then prompts the model to choose the best answer from among them.

Decomposition prompting is a powerful approach that breaks down complex problems into simpler, more manageable sub-tasks. This technique is inspired by a fundamental human problem-solving strategy and has shown remarkable success in enhancing AI performance without requiring larger models

ReAct is a general paradigm that combines reasoning and acting with LLMs. ReAct prompts LLMs to generate verbal reasoning traces and actions for a task. This allows the system to perform dynamic reasoning to create, maintain, and adjust plans for acting while also enabling interaction to external environments (e.g., Wikipedia) to incorporate additional information into the reasoning.
```
Question What is the elevation range for the area that the eastern sector of the
Colorado orogeny extends into?
Thought 1 I need to search Colorado orogeny, find the area that the eastern sector
of the Colorado orogeny extends into, then find the elevation range of the
area.
Action 1 Search[Colorado orogeny]
Observation 1 The Colorado orogeny was an episode of mountain building (an orogeny) in
Colorado and surrounding areas.
Thought 2 It does not mention the eastern sector. So I need to look up eastern
sector.
Action 2 Lookup[eastern sector]
Observation 2 (Result 1 / 1) The eastern sector extends into the High Plains and is called
the Central Plains orogeny.
Thought 3 The eastern sector of Colorado orogeny extends into the High Plains. So I
need to search High Plains and find its elevation range.
Action 3 Search[High Plains]
Observation 3 High Plains refers to one of two distinct land regions
Thought 4 I need to instead search High Plains (United States).
Action 4 Search[High Plains (United States)]
Observation 4 The High Plains are a subregion of the Great Plains. From east to west, the
High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130
m).[3]
Thought 5 High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer
is 1,800 to 7,000 ft.
Action 5 Finish[1,800 to 7,000 ft]
```
<!-- Generate code, test it, analyze failures, and iteratively improve until passing all tests. -->


LLM settings

Temperature - In short, the lower the temperature, the more deterministic the results in the sense that the highest probable next token is always picked. Increasing temperature could lead to more randomness, which encourages more diverse or creative outputs. You are essentially increasing the weights of the other possible tokens. In terms of application, you might want to use a lower temperature value for tasks like fact-based QA to encourage more factual and concise responses. For poem generation or other creative tasks, it might be beneficial to increase the temperature value.
Temperature regulates the unpredictability of a language model's output. With higher temperature settings, outputs become more creative and less predictable as it amplifies the likelihood of less probable tokens while reducing that for more probable ones. Conversely, lower temperatures yield more conservative and predictable results. 

The temperature parameter controls the randomness of the model's output. It adjusts the probability distribution of the next token:

Low temperature (e.g., 0.2): Makes the output more deterministic and focused. The model is more likely to choose high-probability tokens.
High temperature (e.g., 1.0 or above): Increases randomness, leading to more creative but less predictable outputs.



Top P - A sampling technique with temperature, called nucleus sampling, where you can control how deterministic the model is. If you are looking for exact and factual answers keep this low. If you are looking for more diverse responses, increase to a higher value. If you use Top P it means that only the tokens comprising the top_p probability mass are considered for responses, so a low top_p value selects the most confident responses. This means that a high top_p value will enable the model to look at more possible words, including less likely ones, leading to more diverse outputs.
Top-P Also known as Nucleus Sampling is a setting in language models that helps manage the randomness of their output. It works by establishing a probability threshold and then selecting tokens whose combined likelihood surpasses this limit.
For instance, let's consider an example where the model predicts the next word in The cat climbed up the ___. The top five words it might be considering could be tree (probability 0.5), roof (probability 0.25), wall (probability 0.15), window (probability .07) and carpet, with probability of .03.
If we set Top-P to .90, the AI will only consider those tokens that cumulatively add up to at least ~90%. In our case:
Adding tree -> total so far is 50%.
Then adding roof -> total becomes 75%.
Next comes wall, and now our sum reaches 90%.
So, for generating output, the AI will randomly pick one among these three options (tree, roof, and wall) as they make up around ~90 percent of all likelihoods. This method can produce more diverse outputs than traditional methods that sample from the entire vocabulary indiscriminately because it narrows down choices based on cumulative probabilities rather than individual token.

Top P says, “Only consider the possibilities that equal or exceed this value.” 

This parameter is expressed as a number between 0.0 and 1.0, with 1.0 being 100% and 0 being 0%.

The top-p parameter (also known as nucleus sampling) controls the cumulative probability of the tokens considered for generation:

Low top-p (e.g., 0.1): Limits the model to only the most probable tokens, making the output more focused.
High top-p (e.g., 0.9): Includes a wider range of tokens, increasing diversity.
When top-p=1.0, all tokens are considered, effectively disabling nucleus sampling.

Maximum Length
The maximum length is the total # of tokens the AI is allowed to generate. This setting is useful since it allows users to manage the length of the model's response, preventing overly long or irrelevant responses. The length is shared between the USER input in the Playground box and the ASSISTANT generated response. Notice how with a limit of 256 tokens, our PirateGPT from earlier is forced to cut its story short mid-sentence.
Max Length - You can manage the number of tokens the model generates by adjusting the max length. Specifying a max length helps you prevent long or irrelevant responses and control costs.

Context Window (or Context Length / Window Size)
This refers to the maximum number of tokens — units of text (roughly ¾ of a word in English, or about 4 characters) — that a language model can process in total (input + output) at once. It defines how much history, conversation, or document the model can “remember” in one go.Models with larger context windows (like GPT‑4 Turbo with up to 128K tokens, Claude 3 Opus with up to 200K tokens, or Gemini 1.5 Pro with up to 1 million tokens) can handle very long documents or extended conversations without losing earlier information 


Example
Context Window = 32,768 tokens
Your Input Prompt = 8,000 tokens
You set Max Tokens (output) = 10,000
Total = 18,000 tokens → within the 32K limit, so it works.
But if you asked for, say, 30,000 output tokens, the request would exceed the model’s context window and fail 

Context Window is like the model’s working memory capacity in tokens — everything it can process at once.

Max Tokens is like the length limit you place on the response so that it fits within that context window.


A frequency penalty is a setting that discourages repetition in the generated text by penalizing tokens proportionally to how frequently they appear. The more often a token is used in the text, the less likely the AI is to use it again.

The presence penalty is similar to the frequency penalty, but flatly penalizes tokens based on if they have occurred or not, instead of proportionally.

Even when Temperature and Top-P are set completely to zero, the AI may not give the same exact output every time. This is due to randomness in GPU (graphics processing unit) calculations being done in the AI's "brain".


At the heart of an LLM is the ability to produce a list of probabilities of every token of the vocabulary being the next token. These probabilities are then used by the search mechanism you chose.  

Temperature changes how those probabilities are generated, while Top P and Top K change which probabilities we can consider. That consideration step may use “sampling” (because we are picking a sample from a subset of all options based on the chances of that value being next within that subset) or do a beam search. 



---  


Encoder-Decoder models, like T5 or BART, are trained with a sequence-to-sequence objective. Here, the encoder first compresses the input sequence into a latent representation, and then the decoder generates output tokens based on that representation.

https://www.aussieai.com/research/decoding