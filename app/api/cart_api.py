from fastapi import APIRouter, HTTPException,Depends,Request
from sqlalchemy.orm import Session
from app.dependency.service_dependency import  get_cart_service
from app.schema.cart_schema import CreateCart
from app.db.database import get_db

cart_router = APIRouter(prefix="/cart", tags=["Cart"])

@cart_router.post("/create_cart")
def create_cart(create_cart:CreateCart, request=Request,cartservice =Depends(get_cart_service)):
    user_id=request.state.auth.user_id
    cart= cartservice.create_cart(create_cart,user_id=user_id)
    return {"message":"cart created successfully","cart":cart}

@cart_router.get("/get-cart-by-user-id")
def get_cart_by_user_id(user_id:int,cartservice=Depends(get_cart_service)):
    cart= cartservice.get_cart_by_user_id(user_id)
    return {"cart":cart}