from sqlalchemy.orm import Session
from app.model.orderitem_model import OrderItem
from app.schema.order_schema import CreateOrderItem

class OrderItemRepository:
    
    def __init__(self,db_session: Session):
        self.db_session = db_session
        
    def create_order_item_repo(self,create_order_item:CreateOrderItem,order_id:int):
        order_item=OrderItem(
            order_id=order_id,
            restaurant_id =create_order_item.restaurant_id,
            food_id=create_order_item.food_id,
            quantity=create_order_item.quantity,
            price=create_order_item.price
        )
        
        self.db_session.add(order_item)
        self.db_session.flush()
        return order_item
        
    def get_order_item_by_order_id(self, order_id:int):
        orderitem=self.db_session.query(OrderItem).filter(OrderItem.order_id==order_id).first()
        return orderitem
    
    def get_order_item_by_restaurant_id(self, restaurant_id:int):
        orderitem = self.db_session.query(OrderItem).filter(OrderItem.restaurant_id==restaurant_id).first()
        return orderitem
    
    def get_order_item_by_food_id(self, food_id:int):
        orderitem = self.db_session.query(OrderItem).filter(OrderItem.food_id==food_id).first()
        return orderitem