from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.schemas import UsuarioSchema, LoginSchema
from app.auth.models import Usuario
from app.auth.service import registrar_usuario, fazer_login, fazer_login_form, criar_token
from app.dependencies import pegar_sessao, verificar_token

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/get")
async def home():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    return registrar_usuario(usuario_schema, session)

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    return fazer_login(login_schema, session)

@auth_router.post("/login-form")
async def login_form(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(pegar_sessao)):
    return fazer_login_form(dados_formulario.username, dados_formulario.password, session)

@auth_router.get("/refresh")
async def use_refresh_token(usuario: Usuario = Depends(verificar_token)):
    return {
        "access_token": criar_token(usuario.id),
        "token_type": "Bearer"
    }