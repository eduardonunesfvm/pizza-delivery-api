from pydantic import BaseModel
from typing import List, Optional


class PedidoSchema(BaseModel):
    usuario: int 

    class Config:
        from_attributes = True

class ItemPedidoSchema(BaseModel):
    quantidade: int
    sabor: str
    tamanho: str
    preco_unitario: float

    class Config:
        from_attributes = True

class ResponsePedidoSchema(BaseModel):
    id: int
    status: str
    preco: float
    itens: List[ItemPedidoSchema]

    class Config:
        from_attributes = True

class ItemPedidoUpdateSchema(BaseModel):
    quantidade: Optional[int] = None
    sabor: Optional[str] = None
    tamanho: Optional[str] = None
    preco_unitario: Optional[float] = None

    class Config:
        from_attributes = True