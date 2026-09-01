from fastapi import APIRouter,HTTPException,Depends
from app.dependency.service_dependency import get_order_service
from app.schema.order_schema import CreateOrder
from app.db.database import get_db

order_router=APIRouter(prefix="/order",tags=["Order"])

@order_router.post("/create_order")
def create_order(create_order:CreateOrder,orderservice=Depends(get_order_service)):
    order=orderservice.create_order(create_order)
    return {"message":"order created successfully","order":order}

@order_router.get("/get-order-by-restaurant-id")
def get_food_by_restaurant_id(restaurant_id:int,orderservice=Depends(get_order_service)):
    order= orderservice.get_order_by_restaurant_id(restaurant_id)
    return {"order":order}