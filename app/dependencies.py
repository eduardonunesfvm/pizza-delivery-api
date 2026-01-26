from fastapi import Depends, HTTPException
from app.database import Base
from sqlalchemy.orm import sessionmaker, Session
from app.models import Usuario
from jose import jwt, JWTError
from app.main import SECRET_KEY, ALGORITHM, oauth2_schema
from app.database import SessionLocal



# função para abrir e fechar sessão.
def pegar_sessao():
    db = SessionLocal()  # bind com engine já tá no SessionLocal
    try:
        yield db
    finally:
        db.close()

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = dic_info.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")
    #verificar se o token é valido
    #extrair o id do usuário do token
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido")
    return usuario
    
