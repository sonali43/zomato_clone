from fastapi import APIRouter, Depends
from app.dependency.service_dependency import get_restaurant_service
from app.service.restaurant_service import RestaurantService
from app.schema.restaurant_schema import CreateRestaurantRequest


router = APIRouter()

@router.post("/restaurants")
def create_restaurant(restaurant_date: CreateRestaurantRequest, restaurant_service: RestaurantService = Depends(get_restaurant_service)):
    return restaurant_service.create_restaurant(restaurant_date)
    