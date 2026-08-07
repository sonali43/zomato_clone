from app.repo.cartitem_repo import CartItemRepository
from app.schema.cartitem_schema import CreatCartItem

class CartItemService:
    def __init__(self,cartitemrepo=CartItemRepository):
        self.cartitem_repo:CartItemRepository=cartitemrepo
        
    def create_cartitem(self,create_cartitem:CreatCartItem):
        return self.cartitem_repo.creat_cart_item_repo(create_cartitem)