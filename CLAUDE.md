# Desafio Técnico — IA e Automação (KODIE)

Projeto integrador dos módulos de Fundamentos de IA e Automação e Agentes.

## Problema escolhido

Classificação automática de mensagens de clientes (caso 4.1): dúvidas, reclamações e solicitações. Um cliente envia uma mensagem, um modelo de IA interpreta o conteúdo, classifica em uma categoria e um fluxo de automação (n8n) encaminha para o setor responsável.

## Tecnologias

- Back-end: FastAPI (Python)
- IA: modelo via API (OpenAI-compatible) com prompt estruturado e resposta em JSON
- Automação: n8n (webhook → HTTP Request para a API → encaminhamento)
- Documentação: README.md com prints do fluxo n8n

## Estrutura esperada

```
api/                 -> FastAPI application (main.py, prompt, schemas)
n8n/                 -> exported n8n workflow JSON
docs/                -> screenshots of the n8n flow (to be added)
.env.example         -> required environment variables (no real secrets)
README.md            -> full project documentation
```

## Regras

- Nunca commitar chaves de API reais; usar apenas `.env.example`.
- A API deve retornar a classificação da IA em JSON organizado.
- O fluxo n8n deve integrar a API via webhook + HTTP Request.
