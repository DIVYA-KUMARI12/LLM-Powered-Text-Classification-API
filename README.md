# LLM-powered Text Classification API
This project implements a text classification service powered by Large Language Models (LLMs) using FastAPI.
It supports classification, feedback collection, and metrics tracking with evaluation on a benchmark dataset.


---

🚀 Features

/classify → Classify text into predefined categories

/feedback → Collect human feedback on predictions

/metrics → View usage, performance, and feedback statistics

Evaluation harness → Computes accuracy, precision, recall, F1

📂 Project Structure

AI-Engineer-Assignment-Tagbox/
│── app/
│   ├── main.py              # FastAPI entry point
│   ├── routes/              # API endpoints
│   │   ├── classify.py
│   │   ├── feedback.py
│   │   └── metrics.py
│   ├── telemetry/           # Metrics and logging
│   └── prompts/             # Baseline and improved prompts
│
│── eval/
│   ├── dataset.jsonl        # Evaluation dataset
│   ├── run.py               # Evaluation harness
│   └── __init__.py
│
│── tests/
│   ├── test_api.py          # Unit tests for API
│   └── __init__.py
│
│── requirements.txt
│── README.md

⚙️ Installation & Setup

# Clone the repo
git clone https://github.com/DIVYA-KUMARI12/AI-Engineer-Assignment-Tagbox.git
cd AI-Engineer-Assignment-Tagbox

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   
# on Linux/Mac
venv\Scripts\activate      
# on Windows

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload

API will be available at:
👉 http://127.0.0.1:8000

📌 API Endpoints

1. POST /classify

Request:
{
  "text": "The stock market crashed yesterday"
}

Response:
{
  "label": "Finance",
  "confidence": 0.89
}

2. POST /feedback

Request:
{
  "text": "The stock market crashed yesterday",
  "predicted": "Finance",
  "correct": "Economy"
}

Response:
{
  "message": "Feedback recorded"
}

3. GET /metrics

Response:
{
  "total_requests": 120,
  "class_distribution": {"Sports": 30, "Politics": 40, "Finance": 50},
  "feedback_counts": {"correct": 90, "incorrect": 30},
  "latency": {"avg_ms": 120, "p95_ms": 300}
}

📝 Prompt Design

Baseline Prompt (Zero-shot)

Classify the following text into categories: Sports, Politics, Finance, Technology.
Text: {input}

Improved Prompt (Few-shot with role)

You are an expert text classification system.  
Classify the text into **Sports, Politics, Finance, or Technology**.  
Here are examples:
- "The government passed a new law" → Politics  
- "Apple released a new iPhone" → Technology  
- "The stock market crashed yesterday" → Finance  
- "The team won the championship" → Sports  

Now classify: {input}

📊 Evaluation

Run evaluation:

python eval/run.py

Expected metrics (fill after running):

Metric	Baseline Prompt	Improved Prompt

Accuracy	PLACEHOLDER	PLACEHOLDER
Precision	PLACEHOLDER	PLACEHOLDER
Recall	PLACEHOLDER	PLACEHOLDER
F1 Score	PLACEHOLDER	PLACEHOLDER

---

✅ Tests

Run tests with:

pytest tests/

---

🔍 Design Trade-offs & Limitations

Trade-offs

Few-shot prompts increase accuracy but add latency

Feedback stored in memory (for demo) – not persistent in production


Limitations

Uses mock classification (replace with real LLM for production)

Metrics reset on server restart

Dataset limited to small JSONL file

---

👩‍💻 Author

Divya Kumari

LinkedIn

GitHub

---

✨ This project was built as part of the AI Engineer Assignment (Tagbox).
