--Optimizing Performance For reasoning   
Temperature and Token Management  
The model performs best with temperature settings between 0.5-0.7, with lower values (closer to 0.5) producing more consistent mathematical proofs and higher values allowing for more creative problem-solving approaches. Monitor and adjust your token usage based on the complexity of your reasoning tasks - while the default max_completion_tokens is 1024, complex proofs may require higher limits.

Prompt Engineering
To ensure accurate, step-by-step reasoning while maintaining high performance:

DeepSeek-R1 works best when all instructions are included directly in user messages rather than system prompts.
Structure your prompts to request explicit validation steps and intermediate calculations.
Avoid few-shot prompting and go for zero-shot prompting only.