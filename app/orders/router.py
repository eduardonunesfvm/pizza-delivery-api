from fastapi import APIRouter, Depends
from app.auth import router
from app.auth.models import Usuario
from app.dependencies import pegar_sessao, verificar_token
from app.orders.schemas import ItemPedidoSchema, ResponsePedidoSchema, PedidoSchema
from sqlalchemy.orm import Session
from app.orders.service import adicionar_item_pedido, criacao_pedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/get")
def home():
    return {"mensagem": "Você acessou a rota padrão de pedidos", "autenticado": False}

@order_router.post("/criar_pedido")
def criar_pedido(pedido: PedidoSchema, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return criacao_pedido(pedido, session, usuario)

@order_router.post("/pedidos/{id_pedido}/adicionar-item")
def adicionar_item(id_pedido: int, item_pedido_schema: ItemPedidoSchema, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return adicionar_item_pedido(id_pedido, item_pedido_schema, session, usuario)