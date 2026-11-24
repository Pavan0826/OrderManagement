from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    name: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(ge=0)


class OrderRequest(BaseModel):
    customer_name: str = Field(min_length=1)
    items: list[OrderItem] = Field(min_length=1)


class OrderRecord(BaseModel):
    customer_name: str
    items: list[OrderItem]
    total: float = Field(ge=0)


class OrderResponse(OrderRecord):
    order_id: int = Field(gt=0)