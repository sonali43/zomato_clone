from sqlalchemy.orm import Session
from app.model.order_model import Order
from app.schema.order_schema import CreateOrder

class OrderRepository:
    def __init__(self,db_session:Session):
        self.db_session = db_session
        
    def create_order_repo(self,create_order:CreateOrder):
        order=Order(
            user_id=create_order.user_id,
            total_price=create_order.total_price,
            status=create_order.status,
            restaurant_id=create_order.restaurant_id
        )
        try:
            self.db_session.add(order)
            self.db_session.commit()
            self.db_session.refresh(order)
            return order
        except Exception as e:
            self.db_session.rollback()
            raise ValueError(str(e))
    def get_order_by_id(self,order_id:int):
        order=self.db_session.querry(Order).filter(Order.id==order_id).first()
        return order
    
    def get_order_by_restaurant_id(self,restaurant_id:int):
        order=self.db_session.query(Order).filter(Order.restaurant_id==restaurant_id).first()
        return order
    
    def get_order_by_user_id(self,user_id:int):
        order=self.db_session.query(Order).filter(Order.user_id==user_id).all()
        return order