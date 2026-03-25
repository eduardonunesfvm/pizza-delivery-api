# 🍕 Pizza Delivery API

A RESTful API for managing a pizza delivery system, built with **Python** and **FastAPI**.

This project was developed as a learning journey to consolidate real-world backend concepts — from routing and authentication to layered architecture and version control.

<p align="center">
  <img src="../docs/swagger.png" alt="Swagger UI Preview">
</p>

---

## 🚀 Features

- User registration and authentication
- Secure authentication using **JWT (JSON Web Tokens)**
- Protected routes with token verification
- Order creation and management
- Item-level order management (add, update, remove items)
- Data validation with **Pydantic**
- Automatic API documentation with **Swagger (OpenAPI)**
- Layered architecture (router → service → repository)
- Version control with Git & GitHub
- Deployed to production using **Render**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main language |
| FastAPI | Web framework |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| PostgreSQL | Database |
| JWT (python-jose) | Authentication |
| Passlib + bcrypt | Password hashing |
| Uvicorn | ASGI server |
| Alembic | Database migrations |

---

## 📂 Project Structure

```
pizza-delivery-api/
├── app/
│   ├── main.py               # App entry point
│   ├── database.py           # Database connection
│   ├── dependencies.py       # FastAPI dependencies
│   │
│   ├── auth/
│   │   ├── router.py         # Auth endpoints
│   │   ├── service.py        # Business logic
│   │   ├── repository.py     # Database queries
│   │   ├── models.py         # SQLAlchemy models
│   │   └── schemas.py        # Pydantic schemas
│   │
│   └── orders/
│       ├── router.py         # Order endpoints
│       ├── service.py        # Business logic
│       ├── repository.py     # Database queries
│       ├── models.py         # SQLAlchemy models
│       └── schemas.py        # Pydantic schemas
│
├── alembic/                  # Database migrations
├── alembic.ini
├── requirements.txt
└── .gitignore
```

---

## 🌐 Live Demo

🔗 **Production API (Render – free tier):**
https://pizza-delivery-api-t8v2.onrender.com/

> ⚠️ Note: This service is deployed on Render's free tier. After some inactivity, the API may take a few seconds to wake up.

---

## 📘 API Documentation

Once the API is running, access:

- **Swagger UI:** `/docs`
- **ReDoc:** `/redoc`

```
https://pizza-delivery-api-t8v2.onrender.com/docs
```

---

## ⚙️ Running Locally

**1. Clone the repository**
```bash
git clone https://github.com/eduardonunesfvm/pizza-delivery-api.git
cd pizza-delivery-api
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the root:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**5. Run migrations**
```bash
alembic upgrade head
```

**6. Start the server**
```bash
uvicorn app.main:app --reload
```

---

## 📌 Learning Goals

- Understand how REST APIs work end-to-end
- Practice layered architecture (router → service → repository)
- Implement JWT authentication and route protection
- Apply Git branching strategy (feature branches)
- Deploy a backend application to production

---

## 🔮 Next Improvements

- Automated tests
- Role-based access control
- Pagination and filtering
- Improved error handling

---

## 👨‍💻 Author

Developed by **Eduardo Nunes** as a backend learning project.

🔗 [GitHub](https://github.com/eduardonunesfvm) 

---

⭐ If you found this project interesting, feel free to explore the code and follow the evolution!
