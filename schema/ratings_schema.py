from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class schema_products(BaseModel):
    rating: Decimal
    contador: int
    
    