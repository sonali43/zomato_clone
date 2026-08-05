from datetime  import datetime, date,time
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey,Integer,Date
from app.db.database import Base

class Cart(Base):
    __tablename__ = "cart"
    
    id:Mapped[int]=mapped_column(
        Integer, primary_key=True,index=True,autoincrement=True
    )
    user_id:Mapped[int]=mapped_column(
        ForeignKey("users.id"),index=True
    )
    created_at :Mapped[datetime]=mapped_column(
        Date, default=datetime.now()
    )
    is_purchse: Mapped[bool]=mapped_column(
        default=True,nullable=True
    )
    
    
    users=relationship(
        "User",
        back_populates="cart"
    )
    
    cartitem=relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete-orphan"
    )