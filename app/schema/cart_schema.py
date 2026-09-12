from pydantic import BaseModel
from app.enums.cart_status import CartStatus
     
class CreatCartItem(BaseModel):
    cart_id: int
    food_id: int
    quantity: int     
    cart_status:CartStatus

  
class CreateCart(BaseModel):
    user_id : int
    total_price:float
    