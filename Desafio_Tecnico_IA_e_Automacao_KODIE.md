DESAFIO TÉCNICO

## IA e Automação

Transforme um problema do cotidiano em uma solução funcional com Inteligência

Artificial, API e automação.

KODIE | Projeto integrador dos módulos de Fundamentos de IA e Automação e

Agentes

Leia o cenário, escolha um problema e desenvolva uma solução simples, funcional e bem documentada.


## 1. Objetivo do Desafio

O objetivo deste desafio é desenvolver uma solução tecnológica simples que utilize Inteligência Artificial para resolver um problema do cotidiano, integrando uma API de IA a um fluxo de automação.

A proposta é aplicar os conhecimentos adquiridos durante as aulas de fundamentos de IA, engenharia de prompts, integração com APIs e ferramentas de automação, como n8n ou Make.

Antes de começar a desenvolver, compreenda o problema escolhido e pense em como a IA e a automação podem contribuir para uma solução prática.

## 2. Contexto do Caso/Cenário

Imagine uma pequena empresa que recebe diariamente diversas mensagens de clientes com dúvidas, solicitações e reclamações.

Atualmente, uma pessoa precisa ler cada mensagem, identificar o assunto e encaminhá-la manualmente para o setor responsável. Esse processo pode consumir muito tempo e dificultar a organização dos atendimentos.

Diante desse cenário, surge a oportunidade de utilizar Inteligência Artificial para interpretar e classificar as mensagens, enquanto uma ferramenta de automação realiza o encaminhamento das informações.

## 3. Problemas a Serem Investigados

Antes de começar a desenvolver, reflita sobre o cenário:

- Como a Inteligência Artificial pode ajudar a organizar as mensagens?

- Quais informações precisam ser identificadas?

- Como classificar as mensagens de acordo com seu conteúdo?

- Como automatizar o encaminhamento dessas informações?

- Como garantir que a resposta da IA esteja em um formato adequado?

## 4. Casos de Problema (Escolha um)

Caso tenha dificuldade em definir um ponto de partida, escolha um dos cenários abaixo como foco do seu projeto.

## 4.1 — Classificação de Mensagens

Uma empresa recebe mensagens de clientes com diferentes tipos de solicitações, mas não possui um processo organizado para identificar cada assunto. Desenvolva uma solução que utilize IA para analisar e classificar as mensagens em categorias, como dúvidas, reclamações ou solicitações.

## 4.2 — Resumo Automático de Textos

Uma equipe recebe diariamente textos extensos, relatórios ou solicitações e precisa dedicar muito tempo à leitura dessas informações. Desenvolva uma solução que utilize IA para gerar resumos automáticos, destacando os principais pontos de cada texto.

## 4.3 — Organização de Tarefas

Uma equipe recebe diversas solicitações de atividades e precisa organizar o que deve ser feito primeiro. Desenvolva uma solução que utilize IA para interpretar as solicitações, identificar prioridades e organizar as tarefas.


## 4.4 — Assistente de Perguntas Frequentes

Uma empresa recebe constantemente as mesmas dúvidas de seus clientes. Desenvolva uma solução que utilize IA para interpretar perguntas e gerar respostas com base em um conjunto simples de informações fornecidas.

A partir desse contexto, escolha um dos caminhos e pense em como estruturar sua solução.

## 5. Tecnologias Obrigatórias

O projeto deverá utilizar:

## Inteligência Artificial

- Uma API ou modelo de IA de sua preferência.

## Back-end

- Python ou Node.js.

- FastAPI ou Express.

## Automação

- n8n ou Make.

As ferramentas de desenvolvimento com IA, como GitHub Copilot ou OpenCode, poderão ser utilizadas durante a implementação.

## 6. Entrega Esperada

O projeto deverá conter:

- API funcional utilizando FastAPI ou Express.

- Integração com um modelo de IA.

- Prompt estruturado para realizar a tarefa escolhida.

- Resposta da IA em formato organizado, preferencialmente JSON.

- Fluxo de automação funcional utilizando n8n ou Make.

- Integração entre a API e o fluxo de automação.

- Arquivo README.md explicando o projeto.

- Documentação visual do fluxo de automação, com capturas de tela (prints) que comprovem sua implementação e funcionamento.

- Repositório no GitHub: todo o projeto deverá ser publicado em um repositório no GitHub, e o link deverá ser enviado como parte da entrega.

Não é necessário desenvolver uma interface visual completa. O foco principal está na integração entre IA, API e automação.

## 7. Documentação do Fluxo de Automação

Inclua na documentação do projeto prints que demonstrem:

- 1 Fluxo completo: captura de tela mostrando todos os nodes conectados e a estrutura geral da automação.

- 2 Execução bem-sucedida: print de uma execução concluída com sucesso, demonstrando que o fluxo funcionou corretamente.

- 3 Configuração dos nodes: prints individuais de cada node utilizado, mostrando suas configurações e os dados inseridos. Exemplos: Webhook, Edit Fields, HTTP Request, node de IA, entre outros.


- 4 Resultados: print demonstrando os dados recebidos e processados em cada etapa importante do fluxo.

Os prints devem estar organizados e acompanhados de pequenas descrições, explicando a função de cada etapa da automação.

Importante: não basta apresentar apenas o fluxo visual completo. É necessário mostrar também as configurações internas dos nodes utilizados, para que seja possível compreender como a automação foi construída.

A documentação deverá ser incluída no README.md ou em um documento complementar (PDF), junto com os demais arquivos do projeto.

## 8. Estrutura do README.md

O README deverá conter:

- 1 Apresentação da Ideia: explique de onde surgiu sua ideia.

- 2 Problema Escolhido: explique qual cenário você decidiu resolver.

- 3 Solução Proposta: descreva como sua solução funciona e de que forma a IA participa do processo.

- 4 Tecnologias Utilizadas: apresente as ferramentas e tecnologias utilizadas no desenvolvimento.

- 5 Funcionamento do Sistema: explique como a API recebe os dados, como a IA processa as informações e como a automação é executada.

- 6 Como Executar: apresente as instruções necessárias para instalar e executar o projeto.

## 9. Forma de Entrega

A entrega deverá ser realizada por meio de um repositório no GitHub, contendo:

- Código-fonte completo do projeto.

- Arquivo README.md com as informações solicitadas.

- Documentação com os prints do fluxo de automação.

- Arquivo JSON exportado do fluxo do n8n, caso essa ferramenta seja utilizada.

Ao finalizar, envie o link do repositório GitHub para a equipe responsável pela avaliação.

Atenção: não publique chaves de API, senhas ou outras credenciais no repositório. Utilize variáveis de ambiente e disponibilize apenas um arquivo .env.example com os nomes das variáveis necessárias.

## 10. Entrega Opcional — Projeto com Docker

Para os alunos que desejarem ir além, será possível entregar o projeto configurado para execução utilizando Docker.

Nessa modalidade, prepare o ambiente para que a API e a ferramenta de automação possam ser

executadas em containers.

Caso escolha essa opção, inclua no repositório GitHub:

- Dockerfile: arquivo com as instruções para construir a imagem da aplicação.

- Docker Compose: arquivo docker-compose.yml com a configuração dos serviços necessários para executar o projeto.

- Arquivo JSON: exportação do fluxo de automação do n8n, caso essa ferramenta seja utilizada.

- Arquivos de configuração: arquivos necessários para configurar e executar os serviços, como .env.example, sem expor chaves de API ou credenciais.


- Documentação: instruções no README explicando como configurar e executar o projeto utilizando Docker Compose.

Importante: a utilização do Docker é opcional e não será um requisito para a conclusão do desafio. Essa entrega será considerada um diferencial na avaliação.

Caso utilize n8n, recomenda-se que o Docker Compose contemple também sua execução, quando fizer sentido para a arquitetura escolhida.

## 11. Mais Importante

Este desafio não possui uma única resposta correta. O objetivo é desenvolver:

- Pensamento crítico e análise de problemas.

- Construção e utilização de prompts.

- Integração com APIs de Inteligência Artificial.

- Organização e validação de dados.

- Construção de fluxos de automação.

- Capacidade de desenvolver soluções utilizando IA.

Mais do que fazer uma IA responder a uma pergunta, é importante demonstrar como ela pode ser integrada a uma aplicação e utilizada para resolver um problema.

## 12. Observação Final

A Inteligência Artificial não precisa apenas responder. Ela pode interpretar informações, apoiar decisões e automatizar tarefas.

O desafio é transformar esses recursos em uma solução funcional.
