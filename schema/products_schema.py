from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class schema_products(BaseModel):
    titulo: str
    precio_compra: Decimal
    descripcion: Optional[str]=None
    categoria: Optional[str]=None
    url_imagen: Optional[str]=None
    
    