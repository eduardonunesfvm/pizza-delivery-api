from fastapi import APIRouter, Depends
from app.auth import router
from app.auth.models import Usuario
from app.dependencies import pegar_sessao, verificar_token
from app.orders.schemas import ItemPedidoSchema, ResponsePedidoSchema, PedidoSchema
from sqlalchemy.orm import Session
from app.orders.service import adicionar_item_pedido, criacao_pedido, deletar_pedido, finalizando_pedido, visualizando_pedido

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

@order_router.delete("/pedidos/{id_pedido}/deletar")
def remover_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return deletar_pedido(id_pedido, session, usuario)

@order_router.post("/pedidos/{id_pedido}/finalizar-pedido")
def finalizar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return finalizando_pedido(id_pedido, session, usuario)

@order_router.get("/pedidos/{id_pedido}/visualizar-pedido")
def visualizar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return visualizando_pedido(id_pedido, session, usuario)