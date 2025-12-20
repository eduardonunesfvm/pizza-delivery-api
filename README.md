# 🍕 Pizza Delivery API

A simple API for managing pizza orders, developed with **FastAPI** as a study project.

---

## 🚀 Technologies

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite

---

## ▶️ How to run the project

### 1️⃣ Create and activate the virtual environment

```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Install dependencies
bash
Copiar código
pip install fastapi uvicorn sqlalchemy
3️⃣ Start the application
bash
Copiar código
uvicorn main:app --reload
The application will be available at:
👉 http://127.0.0.1:8000

API documentation (Swagger):
👉 http://127.0.0.1:8000/docs

📁 Project structure
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
📌 Project status
🚧 In development — study project.

🧠 Notes
This project is intended for educational purposes, focusing on:

REST API development

Route organization

FastAPI best practices