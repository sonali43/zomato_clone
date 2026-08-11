from datetime import datetime, date, time
from app.enums.order_status import OrderStatus
from app.db.database import Base
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, Float,Enum,DateTime

class Order(Base):
    __tablename__ ="order"
    
    id:Mapped[int]=mapped_column(
      Integer,primary_key=True,index=True,autoincrement=True  
    )
    
    user_id :Mapped[int]= mapped_column(
        ForeignKey("users.id"),index=True
    )
    
    restaurant_id:Mapped[int]=mapped_column(
        ForeignKey("restaurant.id"),index=True
    )
    
    total_price :Mapped[Float]=mapped_column(
        Float,nullable=True
    )
    
    status : Mapped[OrderStatus]=mapped_column(
        Enum(OrderStatus)
    )
    
    created_at :Mapped[datetime]=mapped_column(
        DateTime, default=datetime.now
    )
    
    users = relationship(
        "User",
        back_populates="order"
    )
    
    restaurant = relationship(
        "Restaurant",
        back_populates="order"
    )
    
    orderitem = relationship(
        "OrderItem",
        back_populates="order"
    )