# 🧠 CV Generator com LangChain e LLM

Este projeto é uma aplicação web que utiliza **LangChain** e **OpenAI** para processar currículos em português e gerar uma versão melhorada em inglês, com habilidades técnicas destacadas. A interface web foi construída com **Flask**, e a lógica de processamento com **LangChain** usa uma cadeia sequencial de prompts, integrando uma LLM para gerar os resultados.

🔗 Acesse a aplicação online: [generatecv-s3g3.onrender.com](https://generatecv-s3g3.onrender.com/)

---

## Funcionalidades

A aplicação realiza os seguintes passos:

1. **Tradução automática** do currículo do português para o inglês.
2. **Melhoria de redação** da versão traduzida.
3. **Identificação de duas linguagens de programação principais**.
4. **Geração de uma seção de habilidades técnicas** com base nas linguagens extraídas.

---

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://www.langchain.com/)
- [OpenAI LLM](https://openai.com/)
- HTML + CSS + JavaScript (frontend)
- Deploy: [Render](https://render.com)

---

## ⚙Como rodar localmente

### Pré-requisitos

- Python 3.9+
- Conta e chave da API da OpenAI (`OPENAI_API_KEY`)

### Passos

1. **Clone o repositório**:

```
bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### Passos

2. **Crie um ambiente virtual e ative:**
`
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
`
2. **Instale as dependências:**:
2. **Crie um ambiente virtual e ative:**
`
pip install -r requirements.txt
`
3. **Rode a aplicação:**
`
python app.py
`

---

## Arquitetura da pipeline (LangChain)
A lógica de processamento está no arquivo langchain_pipeline.py e é composta por uma cadeia sequencial de 4 etapas:

Currículo em PT
   ↓
Tradução → step_one
   ↓
Melhoria → step_two
   ↓
Linguagens-chave → step_three
   ↓
Habilidades técnicas → step_four

---

## Estrutura do Projeto

├── app.py                     # Servidor Flask com rotas
├── langchain_pipeline.py     # Lógica da pipeline com LangChain
├── templates/
│   └── index.html            # Interface web
├── static/                   # (caso inclua arquivos estáticos)
├── .env                      # (opcional - configure OPENAI_API_KEY)
└── requirements.txt          # Dependências
