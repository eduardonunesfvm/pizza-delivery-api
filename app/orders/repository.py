from sqlalchemy.orm import Session
from app.orders.models import Pedido, ItemPedido
from app.auth.models import Usuario
from app.orders.schemas import ItemPedidoSchema, PedidoSchema, ItemPedidoUpdateSchema
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
    pedido.calcular_preço()
    session.commit()

def deletar_pedido_repository(id_pedido: int, session: Session):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        return None
    session.delete(pedido)
    session.commit()
    return pedido

def finalizar_pedido(id_pedido: int, session: Session):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        return None
    pedido.status = "FINALIZADO"
    session.commit()
    return pedido

def visualizar_pedido(id_pedido: int, session: Session):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        return None
    return {
         "quantidade_itens_pedido": len(pedido.itens),
         "pedido": pedido
   }

def listar_todos_pedidos_usuario(usuario_id: int, session: Session):
    pedidos_all = session.query(Pedido).filter(Pedido.usuario == usuario_id).all()
    return {
        "quantidade_pedidos": len(pedidos_all),
        "pedidos": pedidos_all
    }

def remover_item_pedido(id_item_pedido: int, session: Session):
    item_pedido = session.query(ItemPedido).filter(ItemPedido.id == id_item_pedido).first()
    if not item_pedido:
        return None
    session.delete(item_pedido)
    session.commit()    
    return item_pedido

def atualizar_item_pedido(id_item: int, item_schema: ItemPedidoUpdateSchema, session: Session):
    item = session.query(ItemPedido).filter(ItemPedido.id == id_item).first()
    if not item:
        return None
    if item_schema.quantidade:
        item.quantidade = item_schema.quantidade
    if item_schema.sabor:
        item.sabor = item_schema.sabor
    if item_schema.tamanho:
        item.tamanho = item_schema.tamanho
    if item_schema.preco_unitario:
        item.preco_unitario = item_schema.preco_unitario
    session.commit()
    return item