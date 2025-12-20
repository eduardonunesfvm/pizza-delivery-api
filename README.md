## Como executar o projeto

### 1️⃣ Ativar o ambiente virtual

```bash
venv\Scripts\activate
2️⃣ Instalar dependências
bash
Copiar código
pip install fastapi uvicorn sqlalchemy
3️⃣ Iniciar a aplicação
bash
Copiar código
uvicorn main:app --reload
A aplicação ficará disponível em:
👉 http://127.0.0.1:8000

Estrutura do projeto
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
Status do projeto
🚧 Em desenvolvimento — projeto de estudo.
