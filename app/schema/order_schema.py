from pydantic import BaseModel
from app.enums.order_status import OrderStatus

class CreateOrderItem(BaseModel):
    restaurant_id : int
    food_id : int
    quantity : int
    price : float
    
class CreateOrder(BaseModel):
    user_id : int
    total_price : float
    restaurant_id : int
    status : OrderStatus
    order_items : list[CreateOrderItem]
    

