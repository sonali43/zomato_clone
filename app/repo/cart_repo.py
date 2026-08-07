from sqlalchemy.orm import Session
from app.model.cart_model import Cart
from app.schema.cart_schema import CreateCart

class CartRepository:
    
    def __init__(self,db_session:Session):
            self.db_session = db_session
            
    def create_cart_repo(self,create_cart:CreateCart):
       cart=Cart(
           user_id=create_cart.user_id,
           total_price=create_cart.total_price
       )
       try:
           self.db_session.add(cart)
           self.db_session.commit()
           self.db_session.refresh(cart)
           return cart
       except Exception as e:
           self.db_session.rollback()
           raise ValueError(str(e))
    def get_cart_by_id(self,cart_id:int):
        cart=self.db_session.query(Cart).filter(Cart.id==cart_id).first()
        return cart
    def get_cart_by_user_id(self,user_id:int):
        cart=self.db_session.query(Cart).filter(Cart.user_id==user_id).all()
        return cart
    