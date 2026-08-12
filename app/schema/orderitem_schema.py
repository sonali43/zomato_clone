from pydantic import BaseModel

class CreateOrderItem(BaseModel):
    order_id = int
    restaurant_id = int
    food_id = int
    quantity = int
    price = float