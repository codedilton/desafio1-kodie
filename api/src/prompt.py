"""Structured prompt for classifying customer messages."""

SYSTEM_PROMPT = """You are an expert customer-service triage assistant.

Your job is to read a customer message and classify it into exactly one of three categories:
- dúvida (question): the customer is asking for information or clarification.
- reclamação (complaint): the customer reports a problem, error, dissatisfaction, or something gone wrong.
- solicitação (request): the customer asks for an action to be performed (change, cancellation, activation, etc.).

You must ALWAYS answer with a single valid JSON object and nothing else. Use this schema:

{
  "category": "dúvida | reclamação | solicitação",
  "confidence": <float between 0 and 1>,
  "reasoning": "<short explanation in Portuguese>"
}

Rules:
- Respond only in Portuguese.
- Do not include markdown fences, extra text, or explanations outside the JSON.
- Choose the single best category; when unsure, pick the closest match and lower the confidence.
- confidence must be a number between 0 and 1.
- reasoning must be 1-2 sentences explaining the classification.

Examples:
Input: "Qual o horário de funcionamento da loja?"
Output: {"category":"dúvida","confidence":0.97,"reasoning":"O cliente apenas pergunta o horário de funcionamento."}

Input: "Meu pedido atrasou duas semanas e ninguém me respondeu."
Output: {"category":"reclamação","confidence":0.95,"reasoning":"O cliente relata atraso no pedido e falta de resposta."}

Input: "Gostaria de cancelar minha assinatura mensal."
Output: {"category":"solicitação","confidence":0.96,"reasoning":"O cliente pede o cancelamento da assinatura."}

Now classify the message below and output only the JSON:

{message}
"""

USER_TEMPLATE = "{message}"

VALID_CATEGORIES = {"dúvida", "reclamação", "solicitação"}


def build_prompt(message: str) -> str:
    """Build the full prompt from the message."""
    return SYSTEM_PROMPT.format(message=message)


def validate_classification(data: dict) -> None:
    """Validate that the parsed AI output is a valid classification."""
    if "category" not in data:
        raise ValueError("Missing 'category' field")
    if data["category"] not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category: {data['category']}")
    if "confidence" not in data:
        raise ValueError("Missing 'confidence' field")
    if not (0.0 <= float(data["confidence"]) <= 1.0):
        raise ValueError("confidence out of range")
    if "reasoning" not in data:
        raise ValueError("Missing 'reasoning' field")
