from sqlalchemy.orm import Session
from app.model.cartitem_model import CartItem
from app.schema.cartitem_schema import CreatCartItem

class CartItemRepository:
    
    def __init__(self,db_session:Session):
        self.db_session = db_session
        
    def creat_cart_item_repo(self,create_cart_item:CreatCartItem):
        cart_item=CartItem(
            cart_id=create_cart_item.cart_id,
            food_id=create_cart_item.food_id,
            quantity=create_cart_item.quantity
        )
        try:
            self.db_session.add(CartItem)
            self.db_session.commit()
            self.db_session.refresh(CartItem)
            return cart_item
        except Exception as e:
            self.db_session.rollback()
            raise ValueError(str(e))
    
    def get_cart_item_by_cart_id(self,cart_id:int):
        cartitem=self.db_session.query(CartItem).filter(CartItem.cart_id == cart_id).first()
        return cartitem