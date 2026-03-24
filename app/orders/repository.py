from sqlalchemy.orm import Session
from app.orders.models import Pedido, ItemPedido
from app.auth.models import Usuario
from app.orders.schemas import ItemPedidoSchema, PedidoSchema
from fastapi import HTTPException

def inserir_pedido(usuario_id: int, session: Session):
    novo_pedido = Pedido(usuario=usuario_id)
    session.add(novo_pedido)
    session.commit()
    return novo_pedido

def inserir_item_pedido(pedido_id: int, item_pedido_schema: ItemPedidoSchema, session: Session):
    pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        return None 
    
    novo_item = ItemPedido(item_pedido_schema.quantidade, item_pedido_schema.sabor, item_pedido_schema.tamanho, item_pedido_schema.preco_unitario, pedido_id)
    session.add(novo_item)
    session.commit()
    return novo_item

def atualizar_preco_pedido(pedido_id: int, session: Session):
    pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
    pedido.calcular_preço()  # chama o método do model
    session.commit()
