
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey,Integer,Float
from app.db.database import Base

class OrderItem(Base):
    __tablename__ = "orderitem"
    
    id:Mapped[int]=mapped_column(
        Integer,primary_key=True,autoincrement=True
    )
    
    order_id:Mapped[int]=mapped_column(
        ForeignKey("order.id"),nullable=False
    )
    
    restaurant_id:Mapped[int]=mapped_column(
        ForeignKey("restaurant.id"),nullable=False
    )
    
    food_id:Mapped[int]=mapped_column(
        ForeignKey("food.id"),nullable=False
    )
    quantity:Mapped[int]=mapped_column(
        Integer
    )
    
    price:Mapped[float]=mapped_column(
        Float
    )
    
    order=relationship(
        "Order",
        back_populates="orderitem"
    )
    
    restaurant=relationship(
        "Restaurant",
        back_populates="orderitem"
    )
    
    food=relationship(
        "Food",
        back_populates="orderitem"
    )