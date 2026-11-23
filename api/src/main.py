"""FastAPI application: message classification backed by an AI model."""

import os
import json
import logging
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from openai import OpenAI

from schemas import ClassifyRequest, ClassifyResponse, Classification, HealthResponse
from prompt import build_prompt, validate_classification

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("classification-api")

app = FastAPI(
    title="Customer Message Classification API",
    description="Classifies customer messages into dúvida, reclamação or solicitação using an AI model.",
    version="1.0.0",
)

client: Optional[OpenAI] = None


@app.on_event("startup")
def _init_client() -> None:
    global client
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    if not api_key or api_key == "your_openai_api_key_here":
        logger.warning("OPENAI_API_KEY not set; AI classification will fall back to a stub.")
        client = None
        return
    kwargs = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    client = OpenAI(**kwargs)


@app.get("/health", response_model=HealthResponse, tags=["health"])
def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="ok")


def _stub_classification(message: str) -> Classification:
    """Offline fallback used when no AI API key is configured.

    Performs simple keyword heuristics so the API remains usable without a key.
    """
    text = message.lower()
    if any(word in text for word in ["erro", "problema", "atraso", "não funcion", "péssimo", "reclama"]):
        category = "reclamação"
        confidence = 0.6
    elif any(word in text for word in ["cancelar", "ativar", "alterar", "solicito", "gostaria de"]):
        category = "solicitação"
        confidence = 0.6
    else:
        category = "dúvida"
        confidence = 0.6
    reasoning = f"Classificação offline (heurística de palavras-chave) para: {message[:60]}..."
    return Classification(category=category, confidence=confidence, reasoning=reasoning)


def _classify_with_ai(message: str) -> Classification:
    """Call the AI model and parse its JSON response."""
    assert client is not None
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    prompt = build_prompt(message)
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )
    content = completion.choices[0].message.content or "{}"
    content = content.strip()
    # Strip accidental markdown fences if the model adds them.
    if content.startswith("```"):
        content = content.split("```", 2)[1] if "```" in content[3:] else content
        if content.startswith("json"):
            content = content[4:]
    data = json.loads(content)
    validate_classification(data)
    return Classification(
        category=data["category"],
        confidence=float(data["confidence"]),
        reasoning=str(data["reasoning"]),
    )


@app.post("/classify", response_model=ClassifyResponse, tags=["classification"])
def classify(request: ClassifyRequest) -> ClassifyResponse:
    """Classify a customer message using the AI model."""
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message must not be empty.")

    try:
        if client is None:
            classification = _stub_classification(message)
        else:
            classification = _classify_with_ai(message)
    except HTTPException:
        raise
    except Exception as exc:  # noqa: BLE001 - surface AI errors as HTTP 502
        logger.exception("Classification failed")
        raise HTTPException(
            status_code=502,
            detail=f"AI classification failed: {exc}",
        ) from exc

    return ClassifyResponse(classification=classification)
