# Sentiment Analysis API

A REST API built with **FastAPI** and a pretrained **Hugging Face DistilBERT** model to classify English text sentiment as **POSITIVE** or **NEGATIVE**, along with a confidence score.

---

## 👩‍💻 Student Information

| Field | Information |
|---|---|
| Full Name | Trương Thị Thảo Ly |
| Student ID | 25127211 |
| Course | Computational Thinking |
| Assignment | LAB 2 – Application Programming Interface |

---

## 📌 Project Overview

This project demonstrates how to integrate a pretrained NLP model into a Web API using FastAPI.

**Main features:**
- Classify English text as `POSITIVE` or `NEGATIVE`.
- Return prediction results and confidence scores in JSON format.
- Validate user input and handle errors.
- Provide interactive API documentation through Swagger UI.

**Hugging Face model:** [DistilBERT SST-2](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)

- **Model ID:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Task:** Sentiment Analysis / Text Classification
- **Language:** English

---

## 🛠️ Project Structure

```text
sentiment-analysis-api/
├── main.py              # FastAPI application and model inference
├── test_api.py          # API testing using requests
├── requirements.txt     # Python dependencies
├── README.md            # Setup and usage guide
└── .gitignore           # Excluded files
```

**Note:** The `.venv/` directory and downloaded model weights are not included in the repository.

---

## 🚀 Installation & Setup

### 1. Prerequisites

- Python 3.13.7 (tested on macOS)
- Internet connection for initial model download

### 2. Clone the Repository

```bash
git clone https://github.com/Tyrhonn/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Start the API Server

```bash
python -m uvicorn main:app --reload
```

The model is automatically downloaded from Hugging Face on the first run.

### 2. Open Swagger UI

Visit:

http://127.0.0.1:8000/docs

Use **Try it out → Execute** to test the API endpoints.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API introduction |
| `GET` | `/health` | Check model availability |
| `POST` | `/predict` | Analyze text sentiment |

### GET /

Returns basic information about the API.

### GET /health

Example response:

```json
{
  "status": "ok",
  "model_loaded": true
}
```

### POST /predict

**Positive example**

Request:

```json
{
  "text": "I love studying computer science!"
}
```

Response:

```json
{
  "input": "I love studying computer science!",
  "label": "POSITIVE",
  "confidence": 0.9996
}
```

**Negative example**

Request:

```json
{
  "text": "This is the worst experience ever!"
}
```

Response:

```json
{
  "input": "This is the worst experience ever!",
  "label": "NEGATIVE",
  "confidence": 0.9998
}
```

The confidence score indicates the model's confidence in its prediction, not its overall accuracy.

---

## 🧪 Testing

Keep the FastAPI server running, then open another terminal:

```bash
python test_api.py
```

The test script uses the `requests` library to verify API functionality and input validation.

| Test Case | HTTP Status | Result |
|---|---|---|
| Home endpoint | `200` | PASS |
| Health endpoint | `200` | PASS |
| Positive prediction | `200` | PASS |
| Negative prediction | `200` | PASS |
| Empty input | `422` | PASS |
| Missing input | `422` | PASS |
| Whitespace-only input | `400` | PASS |

**Local test result:**

```text
All 7 API tests passed!
```

---

## 🎬 Demonstration Video

[Watch the Demonstration Video](VIDEO_LINK_HERE)

---

## ⚠️ Limitations

- Designed for English-language sentiment classification.
- Supports only `POSITIVE` and `NEGATIVE` labels.
- May misclassify sarcastic or ambiguous text.
