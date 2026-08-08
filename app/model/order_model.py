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
    
    total_price :Mapped[Float]=mapped_column(
        Float,nullable=True
    )
    
    status : Mapped[bool]=mapped_column(
        Enum(OrderStatus),default=OrderStatus.PENDING,nullable=True
    )
    
    created_at :Mapped[datetime]=mapped_column(
        DateTime, default=datetime.now
    )
    
    users = relationship(
        "User",
        back_populates="order"
    )