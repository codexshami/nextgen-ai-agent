from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float
    is_available: bool

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool

class ItemListResponse(BaseModel):
    items: list[ItemResponse]
    total: int
