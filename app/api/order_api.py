from fastapi import APIRouter,HTTPException,Depends,Request
from app.dependency.service_dependency import get_order_service
from app.schema.order_schema import CreateOrder
from app.db.database import get_db

order_router=APIRouter(prefix="/order",tags=["Order"])

@order_router.post("/create_order")
def create_order(create_order:CreateOrder,request:Request,orderservice=Depends(get_order_service)):
    user_id=request.state.auth.user_id
    order=orderservice.create_order(create_order,user_id=user_id)
    return {"message":"order created successfully","order":order}
    

@order_router.get("/get-order-by-restaurant-id")
def get_food_by_restaurant_id(restaurant_id:int,orderservice=Depends(get_order_service)):
    order= orderservice.get_order_by_restaurant_id(restaurant_id)
    return {"order":order}

