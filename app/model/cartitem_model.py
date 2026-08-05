from datetime import datetime, date,time
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey,Integer,Date
from app.db.database import Base

class CartItem(Base):
    __tablename__ = "cartitem"
    
    id:Mapped[int]=mapped_column(
        Integer,primary_key=True,autoincrement=True
    )
    cart_id:Mapped[int]= mapped_column(
        ForeignKey("cart.id"),nullable=False
    ) 
    food_id:Mapped[int]= mapped_column(
        ForeignKey("food.id"), nullable=False
    )
    quantity:Mapped[int]=mapped_column(
        Integer
    )
    
    cart=relationship(
        "Cart",
        back_populates="cartitem"
    )
    
    food= relationship(
        "Food",
        back_populates="cartitem"
    )