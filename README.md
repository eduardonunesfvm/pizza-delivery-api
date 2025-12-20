# 🍕 Pizza Delivery API

API simples para gerenciamento de pedidos de uma pizzaria, desenvolvida com **FastAPI** como projeto de estudo.

---

## 🚀 Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite (banco de dados)

---

## ▶️ Como executar o projeto

### 1️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate

2️⃣ Instalar as dependências
pip install fastapi uvicorn sqlalchemy

3️⃣ Iniciar a aplicação
uvicorn main:app --reload


A aplicação ficará disponível em:
👉 http://127.0.0.1:8000

Documentação automática da API:
👉 http://127.0.0.1:8000/docs

📁 Estrutura do projeto
pizza-delivery-api/
├── main.py
├── auth_routes.py
├── order_routes.py
├── models.py
├── venv/
├── .gitignore
└── README.md

📌 Status do projeto

🚧 Em desenvolvimento — projeto de estudo.

🧠 Observações

Este projeto tem fins educacionais, com foco no aprendizado de:

Criação de APIs REST

Organização de rotas

Boas práticas com FastAPI