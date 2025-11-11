# Applied-GenAI-Lab 🚀

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow.svg?logo=huggingface&logoColor=white)](https://huggingface.co/transformers/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜Chain-orange.svg)](https://www.langchain.com/)
[![PEFT](https://img.shields.io/badge/PEFT-LoRA-green.svg)](https://huggingface.co/docs/peft/index)
[![Gradio](https://img.shields.io/badge/Gradio-Demo-lightgrey.svg?logo=gradio)](https://gradio.app/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-black.svg?logo=openai)](https://platform.openai.com/)
[![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented-blueviolet.svg)]()
[![Agents](https://img.shields.io/badge/AI-Agents-red.svg)]()

Welcome to my **Applied-LLM-Engineering-Lab** — a hands-on portfolio of projects showcasing my work in **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Fine-Tuning, and AI Agents**.  

This repo is designed as both a **learning lab** and a **showcase of engineering projects**, demonstrating practical applications of Generative AI for real-world problems.  

---

## 📂 Repo Structure

- **`notebooks/`** → Exploratory notebooks on LLM fundamentals  
- **`rag/`** → Retrieval-Augmented Generation (search + LLM) pipelines  
- **`fine-tuning/`** → Experiments with parameter-efficient fine-tuning (LoRA, PEFT)  
- **`agents/`** → Building autonomous AI agents with LangChain, LlamaIndex, etc.  
- **`utils/`** → Shared utilities for prompts, evaluation, and data loading  
- **`docs/`** → Architecture diagrams, project notes, and showcase visuals  

---

## 🔑 Featured Projects

### 📘 Retrieval-Augmented Generation (RAG)
- **`rag/simple_rag.ipynb`** → Minimal RAG pipeline using FAISS + Llama  
- **`rag/advanced_rag_pipeline/`** → Modular RAG system with retriever, generator, and evaluation  

### 🎯 Fine-Tuning
- **`fine-tuning/peft_finetune.ipynb`** → Fine-tuning with PEFT/LoRA on summarization  
- **`fine-tuning/summarization/`** → Domain-specific summarization fine-tuned model  

### 🤖 AI Agents
- **`agents/langchain_agent.ipynb`** → Basic LangChain agent demo  
- **`agents/multi_agent_demo/`** → Multi-agent collaboration (planner + executor)  

---

## ⚙️ Tech Stack

- **LLMs** → Meta LLaMA, OpenAI GPT, Mistral  
- **Frameworks** → Hugging Face Transformers, LangChain, LlamaIndex  
- **Fine-tuning** → PEFT, LoRA, Transformers Trainer  
- **RAG** → FAISS, Chroma, Pinecone  
- **Agents** → LangChain agents, custom planners/executors  

---

## 🌟 Goals of this Repo

- Demonstrate **practical LLM engineering skills** beyond toy examples  
- Provide **end-to-end workflows**: data prep → model → evaluation → deployment  
- Showcase **breadth** (RAG, fine-tuning, agents) and **depth** (clean code, modular design)  
- Serve as a **personal knowledge base** for future projects  

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+** (required for this project)
- **Git** (for cloning the repository)
- **uv** (Python package installer and resolver) - see installation steps below

### Clone the Repository

```bash
git clone https://github.com/Rathna-Reddy/Applied-GenAI-Lab.git
cd Applied-GenAI-Lab
```

### Installing uv

This project uses **uv** for fast and reliable Python package management. uv is an extremely fast Python package installer and resolver written in Rust, designed as a drop-in replacement for pip and pip-tools.

#### Check if uv is Already Installed

First, check if you already have uv installed on your system:

```bash
uv --version
```

If the command returns a version number (e.g., `uv 0.1.0`), you're all set! Skip to the [Setting Up the Virtual Environment](#setting-up-the-virtual-environment) section.

#### Install uv

If uv is not installed, follow these steps based on your operating system:

**macOS and Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, **restart your terminal** or source your shell profile (e.g., `source ~/.bashrc` or `source ~/.zshrc`) to add uv to your PATH.

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative: Using pip (if you have Python already):**

```bash
pip install uv
```

**Verify Installation:**

```bash
uv --version
```

### Advantages of Using uv

- ⚡ **Extremely Fast**: Written in Rust, uv is 10-100x faster than pip
- 🔒 **Reliable**: Built on top of the same resolver as pip, ensuring compatibility
- 📦 **Complete Toolchain**: Handles virtual environments, package installation, and dependency resolution
- 🔄 **Drop-in Replacement**: Compatible with existing `requirements.txt` and `pyproject.toml` files
- 🎯 **Better Dependency Resolution**: Faster and more reliable dependency resolution
- 🚀 **Modern**: Designed for modern Python projects with support for PEP 517/518 standards

### Setting Up the Virtual Environment

Once uv is installed, create and activate a virtual environment for this project:

```bash
# Create a virtual environment using uv
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
```

### Install Dependencies

Install all project dependencies from `pyproject.toml`:

```bash
uv sync
```

This command will:
- Read dependencies from `pyproject.toml`
- Create or update the `uv.lock` file for reproducible builds
- Install all dependencies in your virtual environment

**Alternative:** If you prefer to install in editable mode without using the lock file:

```bash
uv pip install -e .
```

### Verify Installation

Verify that all packages are installed correctly:

```bash
python -c "import torch; import transformers; import langchain; print('All dependencies installed successfully!')"
```

---

## 👋 About Me

I’m a **Test Automation Engineer** transitioning into **Machine Learning / LLM Engineering**.  
This repo is part of my journey to build a strong portfolio of **applied Generative AI projects**.  

- 🌎 Based in Montreal, Canada  
- 💼 Open to LLM/AI Engineer roles in **Canada & USA**  
- 🔗 Connect with me: [LinkedIn](your-link) | [Email](your-email)  

---

⭐ If you find this repo useful or interesting, please give it a **star** to support my work!  
