"""Pydantic schemas for the message classification API."""

from pydantic import BaseModel, Field


class ClassifyRequest(BaseModel):
    """Incoming customer message to be classified."""

    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="Customer message text to classify",
        example="Minha fatura chegou com o valor errado, gostaria de correção.",
    )


class Classification(BaseModel):
    """Single classification result returned by the AI model."""

    category: str = Field(
        ...,
        description="One of: dúvida, reclamação, solicitação",
        example="reclamação",
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1",
        example=0.93,
    )
    reasoning: str = Field(
        ...,
        description="Short explanation of why this category was chosen",
        example="O cliente relata erro no valor da fatura e pede correção.",
    )


class ClassifyResponse(BaseModel):
    """API response containing the AI classification."""

    classification: Classification


class HealthResponse(BaseModel):
    status: str = "ok"
