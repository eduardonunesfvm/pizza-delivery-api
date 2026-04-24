from sqlalchemy.orm import Session
from app.orders.models import Pedido, ItemPedido
from app.auth.models import Usuario
from app.orders.schemas import ItemPedidoSchema, ItemPedidoUpdateSchema


def buscar_usuario_por_id(usuario_id: int, session: Session):
    return session.query(Usuario).filter(Usuario.id == usuario_id).first()


def buscar_pedido_por_id(pedido_id: int, session: Session):
    return session.query(Pedido).filter(Pedido.id == pedido_id).first()


def buscar_item_por_id(item_id: int, session: Session):
    return session.query(ItemPedido).filter(ItemPedido.id == item_id).first()


def inserir_pedido(usuario_id: int, session: Session):
    novo_pedido = Pedido(usuario=usuario_id)
    session.add(novo_pedido)
    session.commit()
    session.refresh(novo_pedido)
    return novo_pedido


def inserir_item_pedido(pedido_id: int, item_pedido_schema: ItemPedidoSchema, session: Session):
    pedido = buscar_pedido_por_id(pedido_id, session)
    if not pedido:
        return None

    novo_item = ItemPedido(
        item_pedido_schema.quantidade,
        item_pedido_schema.sabor,
        item_pedido_schema.tamanho,
        item_pedido_schema.preco_unitario,
        pedido_id
    )
    session.add(novo_item)
    session.commit()
    session.refresh(novo_item)
    return novo_item


def atualizar_preco_pedido(pedido_id: int, session: Session):
    pedido = buscar_pedido_por_id(pedido_id, session)
    if not pedido:
        return None

    pedido.calcular_preço()
    session.commit()
    session.refresh(pedido)
    return pedido


def deletar_pedido_repository(id_pedido: int, session: Session):
    pedido = buscar_pedido_por_id(id_pedido, session)
    if not pedido:
        return None

    session.delete(pedido)
    session.commit()
    return pedido


def finalizar_pedido(id_pedido: int, session: Session):
    pedido = buscar_pedido_por_id(id_pedido, session)
    if not pedido:
        return None

    pedido.status = "FINALIZADO"
    session.commit()
    session.refresh(pedido)
    return pedido


def visualizar_pedido(id_pedido: int, session: Session):
    pedido = buscar_pedido_por_id(id_pedido, session)
    if not pedido:
        return None

    return {
        "quantidade_itens_pedido": len(pedido.itens),
        "pedido": pedido
    }


def listar_todos_pedidos_usuario(usuario_id: int, session: Session):
    pedidos = session.query(Pedido).filter(Pedido.usuario == usuario_id).all()
    return {
        "quantidade_pedidos": len(pedidos),
        "pedidos": pedidos
    }


def remover_item_pedido(id_item_pedido: int, session: Session):
    item_pedido = buscar_item_por_id(id_item_pedido, session)
    if not item_pedido:
        return None

    session.delete(item_pedido)
    session.commit()
    return item_pedido


def atualizar_item_pedido(id_item: int, item_schema: ItemPedidoUpdateSchema, session: Session):
    item = buscar_item_por_id(id_item, session)
    if not item:
        return None

    if item_schema.quantidade is not None:
        item.quantidade = item_schema.quantidade
    if item_schema.sabor is not None:
        item.sabor = item_schema.sabor
    if item_schema.tamanho is not None:
        item.tamanho = item_schema.tamanho
    if item_schema.preco_unitario is not None:
        item.preco_unitario = item_schema.preco_unitario

    session.commit()
    session.refresh(item)
    return item