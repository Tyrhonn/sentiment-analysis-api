from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline


MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

classifier = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global classifier

    print("Loading Hugging Face model...")

    classifier = pipeline(
        task="text-classification",
        model=MODEL_NAME,
        device=-1
    )

    print("Model loaded successfully!")
    yield

    classifier = None


app = FastAPI(
    title="Sentiment Analysis API",
    description="English text sentiment analysis using DistilBERT.",
    version="1.0.0",
    lifespan=lifespan
)


class TextInput(BaseModel):
    text: str = Field(min_length=1, max_length=2000)


@app.get("/", summary="API Introduction", tags=["System"])
def home():
    return {
        "message": "Welcome to Sentiment Analysis API",
        "model": MODEL_NAME,
        "description": "Predict positive or negative sentiment."
    }


@app.get("/health", summary="Check API Health", tags=["System"])
def health():
    if classifier is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not available"
        )

    return {
        "status": "ok",
        "model_loaded": True
    }


@app.post("/predict", summary="Analyze Text Sentiment", tags=["Sentiment Analysis"])
def predict(data: TextInput):
    text = data.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Input text cannot be empty"
        )

    if classifier is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not available"
        )

    try:
        result = classifier(
            text,
            truncation=True,
            max_length=512
        )[0]

        return {
            "input": text,
            "label": result["label"],
            "confidence": round(
                float(result["score"]), 4
            )
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred during model inference"
        )
