# 🧠 Prompting & Inference Mastery Tracker (GenAI Deep-Dive)

A step-by-step roadmap to mastering prompt engineering, structured reasoning, LLM inference, and optimization.

---

## ✅ Study Plan & Checklist

### 📚 1. Survey & Landscape Mapping
- [ ] Read **Prompt Report 2024** (Schulhoff et al.)
- [ ] Explore **Prompt Engineering Guide** (133+ methods)
- [ ] List 10–20 prompting techniques into a mindmap
- [ ] Understand taxonomy: zero-shot, few-shot, CoT, ReAct, etc.

**💡 Mini-Project:**  
Create a **prompting technique map** in Notion/Miro — group prompts by type, goal, and reliability.

---

### 🧠 2. Prompting Core Techniques
- [ ] Zero-shot prompting
- [ ] Few-shot prompting
- [ ] Chain-of-Thought (CoT)
- [ ] ReAct (Reasoning + Acting)
- [ ] Tree-of-Thought (ToT)
- [ ] Self-Ask / Auto-CoT
- [ ] RAG (Retrieval-Augmented Generation)

**💡 Mini-Project:**  
Build a **prompt playground** to test different techniques on the same problem (e.g., math word problem or text classification).

---

### 🧾 3. Reasoning & Structured Output --> use different libraries to get the structured output
- [ ] Use CoT prompts to break down logic
- [ ] Control formatting (e.g., JSON, Markdown, key-value)
- [ ] Try multi-turn reasoning with CoT or ReAct
- [ ] Compare prompt styles that affect structure (e.g., "return as JSON")

**💡 Mini-Project:**  
Create a **reasoning bot** that takes user input and outputs a structured JSON explanation trace.

---

### ⚙️ 4. Inference Parameters & Controls
- [ ] Learn temperature (randomness)
- [ ] Learn top-p (nucleus sampling)
- [ ] Learn top-k (token restriction)
- [ ] Explore frequency & presence penalties
- [ ] Use stop sequences and max tokens

**💡 Mini-Project:**  
Build a small **UI playground** that lets you tune top-p, temperature, etc., and shows side-by-side output comparisons.

---

### 🚀 5. LLM Inference Systems
- [ ] Learn how inference works (token-by-token)
- [ ] Study KV caching, batching, quantization
- [ ] Try vLLM / llama.cpp / TGI
- [ ] Deploy an LLM API backend (e.g., via FastAPI)

**💡 Mini-Project:**  
Create your own **inference API server** using vLLM or llama.cpp and compare its response latency to OpenAI API.

---

### 🛡️ 6. Prompt Optimization & Guardrails
- [ ] Learn prompt sensitivity and adversarial prompts
- [ ] Study guardrails (delimiters, validation, roles)
- [ ] Try Guidance, GuardrailsAI, or TruLens
- [ ] Design robust system prompts (role control, self-checks)

**💡 Mini-Project:**  
Create an **anti-jailbreak prompt system** that resists prompt injection and logs adversarial attempts.

---

### 🎓 7. Advanced Techniques (Optional)
- [ ] Auto-CoT (automated reasoning prompt creation)
- [ ] Prompt tuning vs prefix tuning vs LoRA
- [ ] Learn soft prompts (embedding-level prompts)
- [ ] Explore instruction tuning and fine-tuning

**💡 Final Challenge:**  
Design a **custom reasoning system** using RAG + Auto-CoT + output formatting + inference optimization.

---

## 🧪 Project List (By Level)

| Level | Project | Description |
|-------|---------|-------------|
| 🟢 Beginner | **Prompt Playground** | Experiment with different prompt types (zero/few-shot, CoT) for one task. |
| 🟡 Intermediate | **Reasoning Assistant** | Output structured logic (e.g., JSON) from a complex query using CoT or ReAct. |
| 🔵 Advanced | **Inference API Server** | Run your own vLLM or llama.cpp backend and expose it with a REST API + UI. |
| 🟣 Expert | **Guardrail & Audit Tool** | Build a prompt + validation system with rejection, retries, and logging. |

---

✅ *Track your progress by checking off each section as you explore and implement techniques.*
