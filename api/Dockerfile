FROM python:3.13-slim

WORKDIR /app

# Dependencies
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY api/src ./src

# Environment
ENV OPENAI_API_KEY=""
ENV OPENAI_MODEL=gpt-4o-mini
ENV OPENAI_BASE_URL=https://api.openai.com/v1
ENV API_HOST=0.0.0.0
ENV API_PORT=8000

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
