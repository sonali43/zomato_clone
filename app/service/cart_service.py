from app.repo.cart_repo import CartRepository
from app.model.cart_model import Cart
from app.schema.cart_schema import CreateCart
class CartService:
    def __init__(self, cartrepo:CartRepository):
        self.cart_repo: CartRepository =cartrepo
        
    def create_cart(self,create_cart:CreateCart):
        return self.cart_repo.create_cart_repo(create_cart)
    
    def get_cart_by_id(self,cart_id:int):
        return self.cart_repo.create_cart_repo(cart_id)
    
    def get_cart_by_user_id(self,user_id:int):
        return self.cart_repo.create_cart_repo(user_id)