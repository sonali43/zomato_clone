from app.repo.orderitem_repo import OrderItemRepository
from app.schema.orderitem_schema import CreateOrderItem

class OrderItemService:
    def __init__(self,orderitemrepo=OrderItemRepository):
        self.orderitem_repo:OrderItemRepository=orderitemrepo
        
    def create_orderitem(self,create_orderitem:CreateOrderItem):
        return self.orderitem_repo.create_order_item_repo(create_orderitem)
    
    def get_orderitem_by_order_id(self,order_id:int):
        return self.orderitem_repo.create_order_item_repo(order_id)
    
    def get_orderitem_by_restaurant_id(self,restaurant_id:int):
        return self.orderitem_repo.create_order_item_repo(restaurant_id)
    
    def get_orderitem_by_food_id(self,food_id:int):
        return self.orderitem_repo.create_order_item_repo(food_id)