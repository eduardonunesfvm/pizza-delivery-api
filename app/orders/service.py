from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.auth.models import Usuario
from app.orders.repository import (
    buscar_usuario_por_id,
    buscar_pedido_por_id,
    atualizar_item_pedido,
    finalizar_pedido,
    inserir_pedido,
    inserir_item_pedido,
    atualizar_preco_pedido,
    deletar_pedido_repository,
    listar_todos_pedidos_usuario,
    remover_item_pedido,
    visualizar_pedido,
)
from app.orders.schemas import (
    ItemPedidoUpdateSchema,
    PedidoSchema,
    ItemPedidoSchema,
)


def criacao_pedido(pedido_schema: PedidoSchema, session: Session, usuario: Usuario):
    if not usuario.admin and usuario.id != pedido_schema.usuario:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    usuario_pedido = buscar_usuario_por_id(pedido_schema.usuario, session)
    if not usuario_pedido:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    novo_pedido = inserir_pedido(pedido_schema.usuario, session)
    return {"mensagem": f"Pedido criado com sucesso {novo_pedido.id}"}


def adicionar_item_pedido(id_pedido: int, item_pedido_schema: ItemPedidoSchema, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    pedido = buscar_pedido_por_id(id_pedido, session)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    item = inserir_item_pedido(id_pedido, item_pedido_schema, session)
    atualizar_preco_pedido(id_pedido, session)

    return item


def deletar_pedido(id_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    pedido = deletar_pedido_repository(id_pedido, session)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    return {"mensagem": f"Pedido número: {id_pedido} deletado com sucesso"}


def finalizando_pedido(id_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    pedido = finalizar_pedido(id_pedido, session)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    return {"mensagem": f"Pedido número: {id_pedido} finalizado com sucesso"}


def visualizando_pedido(id_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    pedido_view = visualizar_pedido(id_pedido, session)
    if not pedido_view:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    return pedido_view


def listar_pedidos_usuario(usuario_id: int, session: Session, usuario: Usuario):
    if not usuario.admin and usuario.id != usuario_id:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    usuario_encontrado = buscar_usuario_por_id(usuario_id, session)
    if not usuario_encontrado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return listar_todos_pedidos_usuario(usuario_id, session)


def remover_item_do_pedido(id_item_pedido: int, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Você não tem autorização para essa operação")

    item = remover_item_pedido(id_item_pedido, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return {"mensagem": f"Item {id_item_pedido} removido com sucesso"}


def update_item_pedido(id_item: int, item_schema: ItemPedidoUpdateSchema, session: Session, usuario: Usuario):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Você não tem autorização")

    item = atualizar_item_pedido(id_item, item_schema, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return {"mensagem": f"Item {id_item} atualizado com sucesso"}