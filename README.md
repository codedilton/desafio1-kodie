# Classificação de Mensagens de Clientes com IA e n8n

Desafio Técnico — IA e Automação (KODIE | Projeto integrador dos módulos de Fundamentos de IA e Automação e Agentes).

## 1. Apresentação da Ideia

Pequenas empresas recebem diariamente dezenas de mensagens de clientes com dúvidas, reclamações e solicitações. Hoje alguém precisa ler cada mensagem, identificar o assunto e encaminhá-la manualmente para o setor responsável — um processo lento e sujeito a erros.

A ideia é automatizar esse triagem: uma API de IA interpreta a mensagem, classifica o assunto e um fluxo de automação no n8n encaminha automaticamente para a equipe certa (suporte, reclamações, atendimento ou revisão manual).

## 2. Problema Escolhido

**Caso 4.1 — Classificação de Mensagens.** Desenvolver uma solução que use IA para analisar e classificar mensagens de clientes em categorias (dúvida, reclamação ou solicitação), integrando uma API de IA a um fluxo de automação que encaminhe as informações ao setor responsável.

## 3. Solução Proposta

A solução tem três partes integradas:

1. **API FastAPI** (`api/`) — recebe a mensagem do cliente pelo endpoint `POST /classify`, envia-a para um modelo de IA com um **prompt estruturado** e retorna a classificação em **JSON** (categoria, confiança e justificativa). Quando nenhuma chave de API está configurada, a API usa um fallback offline baseado em palavras-chave, para que o fluxo continue funcionando em demonstração.

2. **Prompt estruturado** (`api/src/prompt.py`) — instrui o modelo a classificar em uma das três categorias e a responder sempre com um único objeto JSON válido, sem texto extra.

3. **Fluxo n8n** (`n8n/classificacao-mensagens.json`) — webhook recebe a mensagem → chama a API FastAPI → formata o resultado → roteia por categoria (switch) → envia e-mail para o setor correspondente (suporte, reclamações, atendimento) ou para revisão manual.

## 4. Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|------------|
| IA | Modelo via API compatível com OpenAI (ex: gpt-4o-mini) |
| Back-end | FastAPI (Python) + Pydantic |
| Automação | n8n (webhook, HTTP Request, Switch, e-mail) |
| Variáveis de ambiente | python-dotenv + `.env.example` (sem segredos reais no repositório) |

## 5. Funcionamento do Sistema

1. O n8n expõe um webhook (`/webhook/classificar-mensagem`) que recebe a mensagem do cliente.
2. O nó "Extrair Mensagem" prepara o payload.
3. O nó "Classificar com IA (API)" faz um `POST` para `https://sua-api/classify` com a mensagem.
4. A FastAPI chama o modelo de IA com o prompt estruturado, valida o JSON retornado e responde com `{ classification: { category, confidence, reasoning } }`.
5. O nó "Formatar Resultado" extrai categoria, confiança e justificativa.
6. O nó "Rotear por Categoria" direciona a mensagem para o e-mail do setor correto (dúvida → suporte, reclamação → reclamações, solicitação → atendimento) ou para revisão manual quando a confiança/categoria não é reconhecida.

## 6. Como Executar

### Pré-requisitos

- Python 3.10+
- n8n (local ou na nuvem)
- Uma chave de API de modelo de IA (OpenAI ou compatível) — opcional para o fallback offline

### 1. API FastAPI

```bash
cd api
cp .env.example .env
# edite .env e preencha OPENAI_API_KEY (ou deixe para usar o fallback offline)
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

A API fica disponível em `http://localhost:8000` com documentação automática em `/docs`.

### 2. n8n

1. Importe o arquivo `n8n/classificacao-mensagens.json` no n8n (Import → From file).
2. Configure a variável de ambiente `API_BASE_URL` no n8n apontando para sua API (ex: `http://localhost:8000` ou o endereço público da sua API).
3. Ative o fluxo.
4. Envie um `POST` para o webhook do n8n com o corpo:

```json
{ "mensagem": "Minha fatura chegou com o valor errado, gostaria de correção." }
```

5. A classificação será enviada por e-mail para o setor correspondente.

### 3. Testando a API diretamente

```bash
curl -X POST http://localhost:8000/classify \
  -H "Content-Type: application/json" \
  -d '{"message": "Qual o horário de funcionamento?"}'
```

Resposta esperada:

```json
{
  "classification": {
    "category": "dúvida",
    "confidence": 0.97,
    "reasoning": "O cliente apenas pergunta o horário de funcionamento."
  }
}
```

## 7. Documentação do Fluxo de Automação (n8n)

### 7.1 Fluxo completo

O fluxo conecta os seguintes nós:

1. **Receber Mensagem** (Webhook) — entrada da mensagem do cliente via `POST`.
2. **Extrair Mensagem** (Set) — prepara o campo `mensagem` para a API.
3. **Classificar com IA (API)** (HTTP Request) — chama a FastAPI `/classify`.
4. **Formatar Resultado** (Set) — extrai categoria, confiança e justificativa.
5. **Rotear por Categoria** (Switch) — divide por dúvida / reclamação / solicitação / outro.
6. **Enviar para Suporte / Reclamações / Atendimento / Revisão Manual** (Send Email) — encaminha ao setor.

*(A captura de tela do fluxo completo deve ser adicionada aqui: `docs/fluxo-completo.png`)*

### 7.2 Execução bem-sucedida

*(Adicionar print de uma execução concluída com sucesso no n8n: `docs/execucao-sucesso.png`)*

### 7.3 Configuração dos nós

*(Adicionar prints individuais da configuração de cada nó: webhook, HTTP Request, Set, Switch e Send Email: `docs/nodo-webhook.png`, `docs/nodo-http-request.png`, etc.)*

### 7.4 Resultados

*(Adicionar print dos dados recebidos e processados em cada etapa: `docs/resultados.png`)*

## 8. Estrutura do Repositório

```
.
├── CLAUDE.md              # documentação técnica do projeto
├── README.md              # este arquivo
├── api/
│   ├── .env.example       # variáveis de ambiente (sem segredos reais)
│   ├── requirements.txt   # dependências Python
│   └── src/
│       ├── main.py        # aplicação FastAPI
│       ├── schemas.py     # modelos Pydantic
│       └── prompt.py      # prompt estruturado de classificação
├── n8n/
│   └── classificacao-mensagens.json  # exportação do fluxo de automação
└── docs/                  # capturas de tela do fluxo n8n (a adicionar)
```

## 9. Variáveis de Ambiente

Copie `.env.example` para `.env` e preencha:

| Variável | Descrição |
|----------|-----------|
| `OPENAI_API_KEY` | Chave da API de IA (obrigatório para classificação real) |
| `OPENAI_MODEL` | Modelo a usar (padrão: `gpt-4o-mini`) |
| `OPENAI_BASE_URL` | URL base da API de IA (padrão: OpenAI) |
| `API_HOST` / `API_PORT` | Endereço e porta da FastAPI |

**Não comite o arquivo `.env` com chaves reais.** Apenas o `.env.example` deve ficar no repositório.

## 10. Licença

Este projeto foi desenvolvido como parte do desafio técnico da KODIE.
