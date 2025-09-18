# LLM-powered Text Classification API

This project implements a text classification service powered by Large Language Models (LLMs) using FastAPI. It supports classification, feedback collection, and metrics tracking, with evaluation on a small benchmark dataset.

---

## 🚀 Features

- `/classify` → Classify text into predefined categories  
- `/feedback` → Collect human feedback on predictions  
- `/metrics` → View usage, performance, and feedback statistics  
- Evaluation harness → Computes Accuracy, Precision, Recall, F1  

---


## 📂 Project Structure

AI-Engineer-Assignment-Tagbox/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── routes/ # API endpoints
│ │ ├── classify.py
│ │ ├── feedback.py
│ │ └── metrics.py
│ ├── telemetry/ # Metrics and logging
│ └── prompts/ # Baseline and improved prompts
├── eval/
│ ├── dataset.jsonl # Evaluation dataset
│ ├── run.py # Evaluation harness
│ └── init.py
├── tests/
│ ├── test_api.py # Unit tests for API
│ └── init.py
├── requirements.txt
└── README.md

---


## ⚙️ Installation & Setup

1. Clone the repo:
git clone https://github.com/DIVYA-KUMARI12/AI-Engineer-Assignment-Tagbox.git
cd AI-Engineer-Assignment-Tagbox

2. Create a virtual environment:
   python -m venv venv

3. Activate the environment:
   # Linux/Mac
  source venv/bin/activate
  
  # Windows
   env\Scripts\activate

 4. Install dependencies:
    pip install -r requirements.txt

5. Run the FastAPI server:
   uvicorn app.main:app --reload

API will be available at: http://127.0.0.1:8000

## 📌 API Endpoints:
**POST /classify**

Request Example:
{
  "text": "The stock market crashed yesterday"
}

Response:
{
  "class": "Finance",
  "confidence": 0.89,
  "prompt_used": "baseline",
  "latency_ms": 7.2
}

**POST /feedback**

Request Example:
{
  "text": "The stock market crashed yesterday",
  "predicted": "Finance",
  "correct": "Economy"
}

Response:
{
  "status": "received",
  "data": {
    "text": "The stock market crashed yesterday",
    "predicted": "Finance",
    "correct": "Economy"
  }
}

**GET /metrics**

Response Example:
{
  "classification": {
    "total_requests": 3,
    "class_distribution": {"toxic": 1, "spam": 1, "safe": 1},
    "average_latency_ms": 50.0,
    "average_latency_ms_measured": 7.0,
    "p95_latency_ms": 7.3
  },
  "feedback": {
    "total_feedback": 3,
    "correct_count": 2,
    "incorrect_count": 1
  }
}

**GET /healthz**

Response Example:
{
  "status": "ok"
}

## 📝 Prompt Design

Baseline Prompt (Zero-shot):
Classify the following text: Sports, Politics, Finance, Technology.
Text: {input}

Improved Prompt (Few-shot with role):
You are an expert text classification system. Classify the text into Sports, Politics, Finance, or Technology. Examples:

"The government passed a new law" → Politics
"Apple released a new iPhone" → Technology
"The stock market crashed yesterday." → Finance
"The team won the championship" → Sports

Now classify: {input}


## 📊 Evaluation

Evaluation executed using eval/run.py on a small sample dataset.

Results:

Class	Precision	Recall	F1
Toxic	  1.0	    0.43	 0.60
Spam	  1.0	    0.14	 0.25
Safe	  0.38	  1.0    0.55

**Overall Accuracy: 0.50**

Latency:

Average: 8.31 ms

95th Percentile: 11.42 ms

**Observations:**
High precision for Toxic/Spam, but low recall; Safe class has high recall—expected behavior for a baseline model.

**Completed Work**

• Ran python eval/run.py to evaluate the classification API

• Tested API endpoints (/classify, /feedback, /metrics, /healthz) using tests/test_api.py

• Verified that classification, feedback, and metrics are working as expected

## 🔍 Design Trade-offs & Limitations

**Trade-offs:**

• Few-shot prompts increase accuracy but add latency

• Feedback stored in memory (demo purposes)

** Limitations:**

• Uses mock classification (replace with real LLM for production)

• Metrics reset on server restart

• Dataset limited to a small JSONL file

👩‍💻 Author
**Divya Kumari**

• LinkedIn: https://www.linkedin.com/in/divya-kumari-7867461b5/

• GitHub: https://github.com/DIVYA-KUMARI12

✨ Built as part of the AI Engineer Assignment (Tagbox)
