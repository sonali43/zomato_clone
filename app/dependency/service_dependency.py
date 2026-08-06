from fastapi import Depends

from app.db.database import get_db
from app.repo.restaurant_repo import RestaurantRepo
from app.service.restaurant_service import RestaurantService
from app.repo.food_repo import FoodRepository
from app.service.food_service import FoodService
from app.service.cart_service import CartService
from app.repo.cart_repo import CartRepository

def get_restaurant_service(db=Depends(get_db)):
    restaurant_repository = RestaurantRepo(db)
    restaurant_service = RestaurantService(restaurant_repository)
    return restaurant_service

def get_food_service(db= Depends(get_db)):
    food_repository = FoodRepository(db)
    food_service = FoodService(food_repository)
    return food_service

def get_cart_service(db=Depends(get_db)):
    cart_repository = CartRepository(db)
    cart_service = CartService(cart_repository)
    return cart_service