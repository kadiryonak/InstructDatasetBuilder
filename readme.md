# InstructDatasetBuilder

Convert PDF files (and later other formats) into **instruction fine-tuning datasets** for LLMs.

---

## 🔍 Features

- Extracts text from PDF files  
- Splits text into chunks with overlap support  
- Generates **instruction–response pairs**:
  - Summary
  - Factual
  - Analysis
  - Definition
  - Comparison
- Saves dataset in **JSONL** and **CSV** formats  
- Pluggable model wrappers:
  - ✅ Dummy model (for testing)
  - ✅ Ollama (local LLMs such as `mistral`, `llama2`)  

---

## 🛠 Installation

```bash
git clone https://github.com/kadiryonak/InstructDatasetBuilder.git
cd InstructDatasetBuilder

python cli.py \
  --input_path path/to/your.pdf \
  --output_jsonl output_dataset.jsonl \
  --model mistral \
  --lang en \
  --chunk_size 1200 \
  --overlap 150 \
  --num_questions 2 \
  --question_types summary,factual,analysis,definition,comparison
Arguments

--input_path: Input PDF file

--output_jsonl: Output JSONL dataset file

--model: Model name for Ollama (if not set, Dummy model will be used)

--lang: Language (tr or en)

--chunk_size: Maximum characters per chunk

--overlap: Overlapping characters between chunks

--num_questions: Number of questions per type

--question_types: Comma-separated list of question types

📁 Repository Structure

parsers.py — PDF parsing logic

chunking.py — Text chunking utilities

models.py — Model wrappers (Dummy, Ollama)

prompts.py — Prompt templates & builder

utils.py — JSON extraction & helpers

dataset.py — Dataset generator

cli.py — CLI entry point

requirements.txt — Dependencies

.gitignore — Ignored files

🔄 Roadmap

Support for EPUB, DOCX and other formats

Hugging Face transformers integration

Output validation with JSON schema

Data augmentation (translations, variations)

Parallel processing for faster dataset generation
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

pip install -r requirements.txt



---

Do you also want me to add a **usage example with your `aristoteles-poetika.pdf`** (like in your original docstring), so people see a real command immediately?
