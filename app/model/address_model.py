from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.database import Base

class Address(Base):
    __tablename__ = "address"
    
    id:Mapped[int]=mapped_column(
        Integer,primary_key=True,index=True,autoincrement=True
    )
    
    user_id:Mapped[int]=mapped_column(
        ForeignKey("users.id"),nullable=False
    )
    
    house_no:Mapped[str]=mapped_column(
        String(100),nullable=False
    )
    
    street:Mapped[str]=mapped_column(
        String(200),nullable=False
    )
    
    city:Mapped[str]=mapped_column(
        String(200),nullable=False
    )
    
    state:Mapped[str]=mapped_column(
        String(200),nullable=False
    )
    pincode:Mapped[str]=mapped_column(
        String(10),nullable=False
    )
    landmark:Mapped[str|None]=mapped_column(
        String(200),nullable=True
    )
    
    address_type:Mapped[str | None]=mapped_column(
        String(50),nullable=True
    )
    
    
    user = relationship(
        "User",
        back_populates="address"
    )