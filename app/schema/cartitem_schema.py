from pydantic import BaseModel

class CreatCartItem(BaseModel):
    cart_id: int
    food_id: int
    quantity: int