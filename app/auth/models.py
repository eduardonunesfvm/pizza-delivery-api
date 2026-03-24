from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Usuario
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key= True, autoincrement= True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String(128))
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default= False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin