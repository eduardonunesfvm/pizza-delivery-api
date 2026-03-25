from fastapi import HTTPException
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.auth.repository import buscar_usuario_por_email, criar_usuario
from app.auth.schemas import UsuarioSchema, LoginSchema
from app.main import bcrypt_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def criar_token(id_usuario, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub": str(id_usuario), "exp": data_expiracao}
    return jwt.encode(dic_info, SECRET_KEY, ALGORITHM)

def autenticar_usuario(email: str, senha: str, session):
    usuario = buscar_usuario_por_email(email, session)
    if not usuario:
        return False
    if not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

def registrar_usuario(usuario_schema: UsuarioSchema, session):
    if buscar_usuario_por_email(usuario_schema.email, session):
        raise HTTPException(status_code=422, detail="E-mail do usuário já cadastrado")

    senha_hash = bcrypt_context.hash(usuario_schema.senha[:72])
    criar_usuario(usuario_schema.nome, usuario_schema.email, senha_hash, usuario_schema.ativo, usuario_schema.admin, session)
    return {"mensagem": f"usuário cadastrado com sucesso {usuario_schema.email}"}

def fazer_login(login_schema: LoginSchema, session):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado ou credenciais erradas")

    return {
        "access_token": criar_token(usuario.id),
        "refresh_token": criar_token(usuario.id, duracao_token=timedelta(days=7)),
        "token_type": "Bearer"
    }

def fazer_login_form(email: str, senha: str, session):
    usuario = autenticar_usuario(email, senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais erradas")
    
    return {
        "access_token": criar_token(usuario.id),
        "token_type": "Bearer"
    }