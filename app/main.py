from fastapi import FastAPI, status

from app.models import OrderRequest, OrderResponse
from app.repository import OrderRepository
from app.service import OrderService


app = FastAPI(title="Order Management API")
order_repository = OrderRepository()
order_service = OrderService(order_repository)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order_data: OrderRequest) -> OrderResponse:
    return order_service.create_order(order_data)


@app.get("/orders", response_model=list[OrderResponse], status_code=status.HTTP_200_OK)
def list_orders() -> list[OrderResponse]:
    return order_service.list_orders()