from fastapi import APIRouter, HTTPException,Depends
from app.dependency.service_dependency import  get_cartitem_service
from app.schema.cartitem_schema import CreatCartItem
from app.db.database import get_db

cartitem_router=APIRouter(prefix="/cartitem",tags=["CartItem"])

@cartitem_router.post("/create_cart_item")
def create_cartitem(create_cart_item:CreatCartItem,cartitemservice=Depends(get_cartitem_service)):
    cartitem=cartitemservice.create_cart_item(create_cart_item)
    return {"message":"cartitem created succesfully","cartitem":cartitem}