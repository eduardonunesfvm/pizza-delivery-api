# Pizza Delivery API

API backend para um sistema de delivery de pizzaria, desenvolvida como projeto de estudo durante o aprendizado de FastAPI e SQLAlchemy, seguindo um curso em vídeo no YouTube.

## Tecnologias Utilizadas
- Python
- FastAPI
- SQLAlchemy
- Uvicorn
- SQLite
- Git

## Objetivo do Projeto
Aplicar conceitos de desenvolvimento backend com FastAPI, incluindo:
- Criação de rotas REST
- Organização de projeto
- Modelagem de banco de dados com SQLAlchemy
- Versionamento com Git

## Como Executar o Projeto

### Ativar o ambiente virtual
```bash
venv\Scripts\activate
Instalar dependências
bash
Copiar código
pip install fastapi uvicorn sqlalchemy
Iniciar a aplicação
bash
Copiar código
uvicorn main:app --reload
A aplicação ficará disponível em:

cpp
Copiar código
http://127.0.0.1:8000
Estrutura do Projeto
text
Copiar código
pizza-delivery-api/
├── main.py
├── auth_routes.py
├── order_routes.py
├── models.py
├── venv/
├── .gitignore
└── README.md
Status do Projeto
Em desenvolvimento — projeto de estudo.

Copiar código
