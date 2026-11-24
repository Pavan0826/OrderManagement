from app.models import OrderRecord, OrderResponse


class OrderRepository:
    def __init__(self) -> None:
        self._orders: list[OrderResponse] = []
        self._next_order_id = 1

    def save(self, order: OrderRecord) -> OrderResponse:
        saved_order = OrderResponse(
            order_id=self._next_order_id,
            **order.model_dump(),
        )
        self._orders.append(saved_order)
        self._next_order_id += 1
        return saved_order

    def list_all(self) -> list[OrderResponse]:
        return list(self._orders)

    def get_by_id(self, order_id: int) -> OrderResponse | None:
        return next(
            (order for order in self._orders if order.order_id == order_id),
            None,
        )