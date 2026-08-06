from pydantic import BaseModel

class CreateCart(BaseModel):
    user_id : int
    total_price:float
    