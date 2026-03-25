from fastapi import HTTPException
from app.auth.models import Usuario
from app.orders.repository import atualizar_item_pedido, finalizar_pedido, inserir_pedido, inserir_item_pedido, atualizar_preco_pedido, deletar_pedido_repository, listar_todos_pedidos_usuario, remover_item_pedido, visualizar_pedido, atualizar_item_pedido
from app.orders.schemas import ItemPedidoUpdateSchema, PedidoSchema, ItemPedidoSchema, ResponsePedidoSchema
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
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    atualizar_preco_pedido(id_pedido, session)  # manda pro repository salvar
    return item

def deletar_pedido(id_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    pedido = deletar_pedido_repository(id_pedido, session)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    return {"mensagem": f"Pedido número: {id_pedido} deletado com sucesso"}

def finalizando_pedido(id_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    pedido = finalizar_pedido(id_pedido, session)
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não existe")
    
    return {"mensagem": f"Pedido número: {id_pedido} finalizado com sucesso"}

def visualizando_pedido(id_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    pedido_view = visualizar_pedido(id_pedido, session)
    if not pedido_view:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido_view

def listar_pedidos_usuario(usuario_id: int, session: Session):
    if not usuario_id:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    pedidos = listar_todos_pedidos_usuario(usuario_id, session)
    return pedidos

def remover_item_do_pedido(id_item_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização para essa operação.")
    
    item = remover_item_pedido(id_item_pedido, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    return {"mensagem": f"Item {id_item_pedido} removido com sucesso"}

def update_item_pedido(id_item: int, item_schema: ItemPedidoUpdateSchema, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização")
    
    item = atualizar_item_pedido(id_item, item_schema, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    return {"mensagem": f"Item {id_item} atualizado com sucesso"}