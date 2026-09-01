from app.model.order_model import Order
from sqlalchemy.orm import Session
from app.repo.order_repo import OrderRepository
from app.schema.order_schema import CreateOrder, CreateOrderItem
from app.repo.orderitem_repo import OrderItemRepository


class OrderService:
    def __init__(self,orderrepo:OrderRepository,orderitemrepo:OrderItemRepository,db:Session):
        self.order_repo:OrderRepository=orderrepo
        self.orderitem_repo:OrderItemRepository=orderitemrepo
        self.db=db
        
    
    def create_order(self,create_order:CreateOrder):
        try:
            order=self.order_repo.create_order_repo(create_order=create_order)
            for order_item in create_order.order_items:
                self.orderitem_repo.create_order_item_repo(create_order_item=order_item, order_id=order.id)
            self.db.commit()
            return order
        except Exception as e:
            self.db.rollback()
            raise ValueError("try later")
       
    
    def  get_order_by_id(self,order_id:int):
        return self.order_repo.create_order_repo(order_id)
    
    def get_order_by_user_id(self,user_id:int):
        return self.order_repo.create_order_repo(user_id)
    
    def get_order_by_restaurant_id(self,restaurant_id:int):
        return self.order_repo.create_order_repo(restaurant_id)
    
    
