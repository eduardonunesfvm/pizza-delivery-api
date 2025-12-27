from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

# cria a conexao do banco
db = create_engine("sqlite:///banco.db")

# cria a base do banco
Base = declarative_base()

# criar as classes/tabelas do banco

# Usuario
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key= True, autoincrement= True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default= False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO"),
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #pendente, cancelado, finalizado
    usuario = Column("usuarios", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #itens = Column("itens", Integer)

    def __init__(self, usuario, status="pendente", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

# ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

# próximo passo;
# executa a criação dos metadados  do seu banco (cria efetivamente o banco de dados)