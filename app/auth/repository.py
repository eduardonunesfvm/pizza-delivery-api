from sqlalchemy.orm import Session
from app.auth.models import Usuario

def buscar_usuario_por_email(email: str, session: Session):
    return session.query(Usuario).filter(Usuario.email == email).first()

def buscar_usuario_por_id(id: int, session: Session):
    return session.query(Usuario).filter(Usuario.id == id).first()

def criar_usuario(nome: str, email: str, senha_hash: str, ativo: bool, admin: bool, session: Session):
    novo_usuario = Usuario(nome, email, senha_hash, ativo, admin)
    session.add(novo_usuario)
    session.commit()

