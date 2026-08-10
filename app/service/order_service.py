from app.model.order_model import Order
from app.repo.order_repo import OrderRepository
from app.schema.order_schema import CreateOrder

class OrderService:
    def __init__(self,orderrepo:OrderRepository):
        self.order_repo:OrderRepository=orderrepo
        
    def create_order(self,create_order:CreateOrder):
        return self.order_repo.create_order_repo(create_order)
    
    def  get_order_by_id(self,order_id:int):
        return self.order_repo.create_order_repo(order_id)
    
    def get_order_by_user_id(self,user_id:int):
        return self.order_repo.create_order_repo(user_id)
    
    def get_order_by_restaurant_id(self,restaurant_id:int):
        return self.order_repo.create_order_repo(restaurant_id)