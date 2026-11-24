from app.models import OrderRecord, OrderRequest, OrderResponse
from app.repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def create_order(self, order_data: OrderRequest) -> OrderResponse:
        total = round(
            sum(item.quantity * item.unit_price for item in order_data.items),
            2,
        )
        order = OrderRecord(
            customer_name=order_data.customer_name,
            items=order_data.items,
            total=total,
        )
        return self._repository.save(order)

    def list_orders(self) -> list[OrderResponse]:
        return self._repository.list_all()

    def get_order(self, order_id: int) -> OrderResponse | None:
        return self._repository.get_by_id(order_id)