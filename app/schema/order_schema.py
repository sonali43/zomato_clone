from pydantic import BaseModel
from app.enums.order_status import OrderStatus

class CreateOrder(BaseModel):
    user_id : int
    total_price : float
    restaurant_id : int
    status : OrderStatus