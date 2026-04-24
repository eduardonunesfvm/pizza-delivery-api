from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pathlib import Path
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware



BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

app = FastAPI(
    title="Pizza Delivery API",
    version="1.0.0",
    description="API REST para gerenciamento de pedidos de uma aplicacao de delivery"
)

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "https://seu-front.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Bem-vindo a Pizza Delivery API ",
        "docs": "/docs",
        "redoc": "/redoc",
        "routes": {
            "/auth": "Autenticacao de usuarios",
            "/usuarios": "Gerenciamento de usuarios",
            "/pedidos": "Operacoes de pedidos"
        }
    }

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from app.auth.router import auth_router
from app.orders.router import order_router

app.include_router(auth_router)
app.include_router(order_router)