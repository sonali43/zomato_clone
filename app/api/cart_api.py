from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from app.dependency.service_dependency import  get_cart_service
from app.schema.cart_schema import CreateCart
from app.db.database import get_db

cart_router = APIRouter(prefix="/cart", tags=["Cart"])

@cart_router.post("/create_cart")
def create_cart(create_cart:CreateCart, cartservice =Depends(get_cart_service)):
    cart= cartservice.create_cart(create_cart)
    return {"message":"cart created successfully","cart":cart}

