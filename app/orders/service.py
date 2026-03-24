from fastapi import HTTPException
from app.auth.models import Usuario
from app.orders.repository import inserir_pedido, inserir_item_pedido, atualizar_preco_pedido
from app.orders.schemas import PedidoSchema, ItemPedidoSchema, ResponsePedidoSchema
from sqlalchemy.orm import Session
from app.orders.models import Pedido, ItemPedido
from typing import List


def criacao_pedido(pedido_schema: PedidoSchema, session: Session, usuario: Usuario):
    if not usuario.admin and usuario.id != pedido_schema.usuario:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    novo_pedido = inserir_pedido(usuario.id, session)
    return {"mensagem": f"Pedido criado com sucesso {novo_pedido.id}"}

def adicionar_item_pedido(id_pedido: int, item_pedido_schema: ItemPedidoSchema, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    item = inserir_item_pedido(id_pedido, item_pedido_schema, session)
    if not item:
        raise HTTPException(status_code=400, detail="Pedido não existe")
    
    atualizar_preco_pedido(id_pedido, session)  # manda pro repository salvar
    return item