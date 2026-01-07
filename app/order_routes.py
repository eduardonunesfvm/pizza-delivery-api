from fastapi import APIRouter, Depends, HTTPException
from app.schemas import PedidoSchema
from app.dependencies import pegar_sessao
from sqlalchemy.orm import Session
from app.models import Pedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos!"}


@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso {novo_pedido.id}"}