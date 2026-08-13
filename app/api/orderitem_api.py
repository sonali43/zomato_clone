from fastapi import HTTPException,APIRouter,Depends
from app.dependency.service_dependency import get_orderitem_service
from app.schema.orderitem_schema import CreateOrderItem
from app.db.database import get_db

orderitem_router=APIRouter(prefix="/orderitem",tags=["OrderItem"])

@orderitem_router.post("/create-orderitem")
def create_orderitem(create_orderitem:CreateOrderItem,order_item_service=Depends(get_orderitem_service)):
    orderitem=order_item_service.create_orderitem(create_orderitem)
    return {"message":"orderitem created successfully","orderitem":orderitem}

@orderitem_router.get("/get-orderitem-by-restaurant-id")
def get_order_item_by_restaurant_id(restaurant_id:int,order_item_service=Depends(get_orderitem_service)):
    orderitem= order_item_service.get_orderitem_by_restaurant_id(restaurant_id)
    return {"orderitem":orderitem}