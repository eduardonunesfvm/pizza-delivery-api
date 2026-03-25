from fastapi import APIRouter, Depends
from app.auth import router
from app.auth.models import Usuario
from app.dependencies import pegar_sessao, verificar_token
from app.orders.models import Pedido
from app.orders.repository import atualizar_item_pedido
from app.orders.schemas import ItemPedidoSchema, ItemPedidoUpdateSchema, ResponsePedidoSchema, PedidoSchema
from sqlalchemy.orm import Session
from app.orders.service import adicionar_item_pedido, criacao_pedido, deletar_pedido, finalizando_pedido, listar_pedidos_usuario, remover_item_do_pedido, update_item_pedido, visualizando_pedido

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

@order_router.get("/pedidos/listar/{usuario_id}")
def get_pedidos_usuario(usuario_id: int, session: Session = Depends(pegar_sessao)):
    return listar_pedidos_usuario(usuario_id, session)

@order_router.delete("/pedido/remover-item/{id_item_pedido}")
def remover_item_pedido(id_item_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return remover_item_do_pedido(id_item_pedido, session, usuario)

@order_router.patch("/pedidos/item/{id_item}")
def atualizar_item(id_item: int, item_schema: ItemPedidoUpdateSchema, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    return update_item_pedido(id_item, item_schema, session, usuario)