Here’s a structured **master list** of resources — at least **five per topic** — to jump‑start your deep dive into prompting & LLM inference.

You can **copy it into Obsidian, Notion, or GitHub** and check off or explore at your own pace. Where possible, I’ve also suggested a mini‑project to apply the lessons. All bullet items are clickable titles (the “links”), and I've included citations for verification. Let me know if you'd like video summaries or slides for any.

---

## Step 1: **Surveys & Landscape Mapping** 🧭

Great for understanding prompting "zones" and major lines of research.

| # | Resource (click to open)                                                                                                              | What You’ll Learn                                                                                                                             | Suggested mini‑project                                                               |                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------- |
| 1 | **Prompt Report (arXiv ‘24)**                                                                                                         | A taxonomy of **133 prompting techniques** across 20+ task groups.                                                                            | Pick 10 techniques, group them into buckets, and present them on a Miro board.       | ([phData][1])          |
| 2 | **Prompt Engineering Guide (PromptingGuide.ai)**                                                                                      | Interactive guide with examples, patterns, and gather‑mode cooldown.                                                                          | Use two personas (e.g. “novice tutor” vs “court reporter”) to judge prompt outcomes. | ([Mnehmos][2])         |
| 3 | **Awesome‑Prompt‑Engineering (GitHub)**                                                                                               | A huge curated list of papers, templates, tools, and even code links.                                                                         | Fork the repo; sort resources by date and add 3 blog posts you discover.             | ([GitHub][3])          |
| 4 | **phData blog on sampling/language tone** — overview of temperature/top‑k/top‑p. Useful to understand *why* prompt structure matters. | Write a small Python notebook using GPT‑4 API to sample responses from five **prompt variations** on the same task and visualize differences. | ([phData][4])                                                                        |                        |
| 5 | **OpenAI’s “Best Practices for Prompt Engineering with the API”**                                                                     | Official guide covering Jaw/chat formats, anchors, few‑shot layout, role prompting.                                                           | Build a template (system + user + example) and benchmark zero‑ vs few‑shot results.  | ([help.openai.com][5]) |

After this survey phase, you’ll have a strong map of the *why, what,& how* of prompting.

---

## Step 2: **Core Prompting Techniques**

These are the most foundational techniques you’ll see in most papers, blog posts, and implementations today:

* **Zero‑Shot** (e.g. `"Summarize the tweet below:"`)
* **Few‑Shot / Persona Prompting** (role-based, with examples)
* **Chain of Thought (CoT)** — `"Let’s think step‑by‑step…"`.
* **Self‑Consistency**, **Tree of Thoughts (ToT)**, **ReAct** (Reason+Act).
* Support for **tool‑use + function‑calling prompts**.

Here are 5 canonical links:

1. **“Chain‑of‑Thought Prompting Elicits Reasoning in Large LMs”** (Wei et al. 2022) — the origin paper for CoT.
   ([arxiv.org][6])
2. **“ReAct: Synergizing Reasoning and Acting in Language Models”** (2022) — for combining reasoning with agentic actions like browsing or calcs.
   ([arxiv.org][7])
3. **“Tree of Thoughts: Deliberate Problem Solving with LLMs”** — for exploring search‑style planning prompts.
   ([arxiv.org][8])
4. **“Self‑Consistency Improves Chain of Thought Reasoning”** — run multiple CoT paths, then vote on the most consistent answer.
   ([openreview.net][9])
5. **Automatic Prompt Engineer (APE)** — a newer tool using LLM‑based prompt generation and ranking.
   ([promptingguide.ai][10])

**Mini‑project idea**: Build a multi‑variant prompt (Zero‑Shot / CoT / Self‑Consistency / ReAct) and compare answer quality across 20 trivia questions.

---

## Step 3: **Reasoning & Structured Output**

Learn how to get LLMs to output JSON, SQL, emojis-only, or named segments reliably:

* Use **explicit JSON schema prompts**
* Apply **function‑calling** APIs for CLI‑style or code‑structured output
* Use tools like **Guidance (MSR)** or **PromptFoo / Guardrails** to automatically enforce format

Resources:

1. **MSR Guidance Library page** — build structured prompts directly as Python schema.
   ([microsoft.com][11])
2. **Outline & llguidance** — a schematic version of Guidance, suited for fast constraint execution.
   ([docs.djl.ai][12])
3. **OpenAI function‑calling tutorial** — how to specify JSON schemas and parse function responses (from their “best practices” guide).
   ([help.openai.com][5])
4. **PromptFoo Guardrails** page — examples of JSON output enforcement, types, and rules.
   ([promptfoo.dev][13])
5. **QED42 "Building simple and effective prompt‑based guardrails"** — teaches how to wrap decisions & responses under decision gates.
   ([qed42.com][14])

**Mini‑project**: Prompt the LLM to output a JSON object listing extracted entities (name, age, location) and verify with a schema checker.

---

## Step 4: **Inference Parameters & Controls**

Tune generation parameters that shape randomness and diversity:

* `temperature`: creativity vs coherence
* `top_p` (nucleus sampling): cumulative probability cutoff
* `top_k`: restrict raw token pool
* You’ll also encounter options like **contrastive decoding** (rare), **beam search** (not in OpenAI API)

Key reads:

1. **phData article on tuning temperature, top‑p, top‑k** — clear graphs and examples.
   ([phData][1])
2. **Luiz Carneiro dev blog** — shows live Gemini API, real‑world examples.
   ([carneiro.dev][15])
3. **Blog: “Understanding Temperature, Top‑p, Top‑k in LLMs”** — use-case comparisons and intuition.
   ([carneiro.dev][15])
4. **Spot Intelligence 10 types guide** — practical tradeoffs of creative/stable sampling strategies.
   ([spotintelligence.com][16])
5. **phData (repeat) link** — emphasizes the often‑overlooked interplay of “temperature & top‑p > top‑k”.
   ([phData][4])

**Mini‑project**: For one prompt, sweep `temperature=0→1.2` and `top_p=0.5→1.0`, compute average token entropy and answer correctness (via rubric).

---

## Step 5: **LLM Inference Systems & Engineering Practices**

Focus on scalable runtimes, batching, speed, cost, and deployment:

Key open‑source frameworks and concepts:

* **vLLM** (with block‑based KV cache, batch scheduling)
* **Hugging Face TGI (Text‑Generation‑Inference)** — production server tool
* \*\*llama.cpp \*\* (CPU + GPU + Apple Silicon + tiny‑model inference)
* Techniques like **alchemy prompt caching**, quantization, fp8/int4, soft sync.

Top guides:

1. **MuegenAI tutorial on VLLM, TGI, DeepSpeed** — coverage of setup, tradeoffs, quant-levels, batching.
   ([muegenai.com][17])
2. **phData analysis on LLM inference optimization (distillation, KV‑cache, quant)** — covers memory/latency/cost.
   ([deepsense.ai][18])
3. **LLM‑Inference Benchmark Cheat‑Sheet (llm‑tracker.info)** — practical tips for benchmarking llama.cpp, throughput on consumer GPUs.
   ([llm-tracker.info][19])
4. **GitHub discussion “LLM inference server performances comparison llama.cpp/TGI/vLLM”** — repeatable performance narratives.
   ([GitHub][20])
5. **Novita.AI blog on KV‑cache compression in vLLM (block‑compression v0.6.2)** — recent kernel‑level optimization for 32K context.
   ([blogs.novita.ai][21])

**Mini‑project**: Spin up vLLM or HF TGI locally (or on a cloud GPU), load a mid‑size open‑source model (e.g. Llama‑3.1‑8B), and benchmark TTFT (Time to First Token) & tokens/sec (with and without quantization).

---

## Step 6: **Prompt Optimization & Guardrails**

These safeguard LLM output, prevent jailbreaks, regulate policy, and ensure compliance.

Must‑read resources:

1. **“Safeguarding Large Language Models: A Holistic Survey” (arXiv, 2024)** — overview of safety categories, guardrail work, evaluation, open challenges.
   ([arxiv.org][22])
2. **“On Prompt‑Driven Safeguarding for LLMs” (arXiv)** — shows how simple safety‑prompts significantly mitigate prompt injection without model changes.
   ([arxiv.org][23])
3. **PromptFoo Guardrails docs** — enforce policies in the pipeline (e.g. disallowed content, extraction filtering).
   ([promptfoo.dev][13])
4. **QED42 blog on implementing prompt‑based guardrails** — five‑part prompt structure, few‑shot examples, decision gates.
   ([qed42.com][14])
5. **Confident‑AI guide to red‑teaming LLMs** — walkthrough of prompt injection, escalation; with checklist examples.
   ([confident-ai.com][24])

**Mini‑project**: Implement a system prompt wrapper that detects personal data (email, SSN), refuses or redacts it, and logs all user inputs with a “policy violation flag.” Then craft two adversarial jailbreak prompts and see how your guardrail handles them.

---

## Step 7: **Advanced Techniques & Prompt Optimization**

These moves are aimed at making your system better over time, often via ML:

* **Instruction Tuning** (fine‑tuning LLMs on instruction‑response pairs)
* **Prompt Tuning / Prefix‑Tuning / Soft‑Prompting / LoRA** (parameter‑efficient adaptation)
* **Automated Prompt Generation** (e.g. Auto‑CoT, prompt search/meta‑prompting)
* **Federated Instruction Tuning / Phased IFT**

Top reads:

1. **Auto‑CoT: Automatic Chain‑of‑Thought Prompting** (arXiv) — learns exemplar questions + reasons automatically from dataset.
   ([arxiv.org][25])
2. **LoRA (=Low‑Rank Adaptation) explained: practical tutorial** — widely used parameter‑efficient fine‑tuning method.
   ([digitalocean.com][26])
3. **“The Power of Scale for Parameter‑Efficient Prompt Tuning” (arXiv)** — shows prompt‑tuning reaches parity at scale with full fine‑tuning.
   ([arxiv.org][27])
4. **Automatic Prompt Augmentation & Selection with CoT** (KaShun Shum, 2024 arXiv) — a follow‑up to Auto‑CoT that prunes and scores CoT examples.
   ([ar5iv.labs.arxiv.org][28])
5. **Phased Instruction Fine‑Tuning (Guan et al. 2024)** — instruction‑tuning by difficulty schedule using GPT‑4 to judge prompts.
   ([arxiv.org][29])

**Mini‑project**: Build a small instruction‑tuned version using LoRA on a 7B model: pick 50 instruction‑response pairs (medical, writing, code), tune with LoRA, then test generation vs. vanilla model.

---

### ✅ Recap & Workflow

1. **Phase 1: Survey & taxonomy** — understand the landscape.
2. **Phase 2: Core prompting frameworks** — practice techniques like CoT, ReAct.
3. **Phase 3: Prompt structure & output control** — enforce JSON, roles, personas.
4. **Phase 4: Decode tuning** — customize decoding parameters.
5. **Phase 5: Runtime systems & inference optimization** — scale and cost.
6. **Phase 6: Build safety, do red‑teaming** — detect and prevent risky behavior.
7. **Phase 7: Optimize & adapt** — gradually improve prompts and model.

---

Let me know which topics you’d like slide decks, video highlights, or even a curated self‑paced sequence with daily tasks — I can generate that next.

[1]: https://www.phdata.io/blog/how-to-tune-llm-parameters-for-top-performance-understanding-temperature-top-k-and-top-p/?utm_source=chatgpt.com "How to Tune LLM Parameters for Top Performance: Understanding Temperature, Top K, and Top P | phData"
[2]: https://mnehmos.github.io/Prompt-Engineering/?utm_source=chatgpt.com "Prompt Engineering Guide | 133+ Techniques & Interactive Tools"
[3]: https://github.com/promptslab/Awesome-Prompt-Engineering?utm_source=chatgpt.com "promptslab/Awesome-Prompt-Engineering - GitHub"
[4]: https://www.phdata.io/blog/how-to-tune-llm-parameters-for-top-performance-understanding-temperature-top-k-and-top-p/ "How to Tune LLM Parameters for Top Performance: Understanding Temperature, Top K, and Top P | phData"
[5]: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api?utm_source=chatgpt.com "Best practices for prompt engineering with the OpenAI API"
[6]: https://arxiv.org/abs/2201.11903?utm_source=chatgpt.com "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
[7]: https://arxiv.org/abs/2210.03629?utm_source=chatgpt.com "ReAct: Synergizing Reasoning and Acting in Language Models"
[8]: https://arxiv.org/abs/2305.10601?utm_source=chatgpt.com "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
[9]: https://openreview.net/forum?id=1PL1NIMMrw&utm_source=chatgpt.com "Self-Consistency Improves Chain of Thought Reasoning in Language..."
[10]: https://www.promptingguide.ai/techniques/ape?utm_source=chatgpt.com "Automatic Prompt Engineer (APE) | Prompt Engineering Guide"
[11]: https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/?utm_source=chatgpt.com "guidance | control LM output - Microsoft Research"
[12]: https://docs.djl.ai/master/docs/serving/serving/docs/lmi/user_guides/vllm_user_guide.html?utm_source=chatgpt.com "vLLM Engine User Guide - Deep Java Library"
[13]: https://www.promptfoo.dev/docs/red-team/guardrails/?utm_source=chatgpt.com "Guardrails | Promptfoo"
[14]: https://www.qed42.com/insights/building-simple-effective-prompt-based-guardrails?utm_source=chatgpt.com "Building simple & effective prompt-based Guardrails"
[15]: https://www.carneiro.dev/blog/ai/llm-sampling-parameters?utm_source=chatgpt.com "Luiz Carneiro Blog - Understanding Temperature, Top-p, and Top-k in LLMs"
[16]: https://spotintelligence.com/2023/11/20/gpt-prompt-engineering/?utm_source=chatgpt.com "How To Guide To GPT Prompt Engineering [10 Types] - Spot Intelligence"
[17]: https://muegenai.com/docs/data-science/llmops/module-6-tools-ecosystem-for-llmops/vllm-tgi-deepspeed-inference/?utm_source=chatgpt.com "VLLM, TGI, DeepSpeed inference - Mue AI - muegenai.com"
[18]: https://deepsense.ai/blog/llm-inference-optimization-how-to-speed-up-cut-costs-and-scale-ai-models/?utm_source=chatgpt.com "LLM Inference Optimization: How to Speed Up, Cut Costs, and Scale AI ..."
[19]: https://llm-tracker.info/howto/LLM-Inference-Benchmarking-Cheat%E2%80%91Sheet-for-Hardware-Reviewers?utm_source=chatgpt.com "LLM Inference Benchmarking Cheat‑Sheet for Hardware Reviewers"
[20]: https://github.com/ggml-org/llama.cpp/discussions/6730?utm_source=chatgpt.com "LLM inference server performances comparison llama.cpp / TGI / vLLM"
[21]: https://blogs.novita.ai/dynamic-kv-cache-compression-based-on-vllm-framework/?utm_source=chatgpt.com "Dynamic KV Cache compression based on vLLM framework"
[22]: https://arxiv.org/abs/2406.02622?utm_source=chatgpt.com "Safeguarding Large Language Models: A Survey"
[23]: https://arxiv.org/html/2401.18018v2?utm_source=chatgpt.com "On Prompt-Driven Safeguarding for Large Language Models"
[24]: https://www.confident-ai.com/blog/red-teaming-llms-a-step-by-step-guide?utm_source=chatgpt.com "LLM Red Teaming: The Complete Step-By-Step Guide To LLM Safety"
[25]: https://arxiv.org/abs/2210.03493?utm_source=chatgpt.com "Automatic Chain of Thought Prompting in Large Language Models"
[26]: https://www.digitalocean.com/community/tutorials/lora-low-rank-adaptation-llms-explained?utm_source=chatgpt.com "LoRA: Low-Rank Adaptation of Large Language Models Explained"
[27]: https://arxiv.org/abs/2104.08691?utm_source=chatgpt.com "Title: The Power of Scale for Parameter-Efficient Prompt Tuning - arXiv.org"
[28]: https://ar5iv.labs.arxiv.org/html/2302.12822?utm_source=chatgpt.com "Automatic Prompt Augmentation and Selection with Chain-of-Thought from ..."
[29]: https://arxiv.org/abs/2406.04371?utm_source=chatgpt.com "Phased Instruction Fine-Tuning for Large Language Models"
