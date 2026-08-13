from fastapi import Depends
from app.db.database import get_db
from app.repo.restaurant_repo import RestaurantRepo
from app.service.restaurant_service import RestaurantService
from app.repo.food_repo import FoodRepository
from app.service.food_service import FoodService
from app.service.cart_service import CartService
from app.repo.cart_repo import CartRepository
from app.service.cartitem_service import CartItemService
from app.repo.cartitem_repo import CartItemRepository
from app.repo.order_repo import OrderRepository
from app.service.order_service import OrderService
from app.repo.orderitem_repo import OrderItemRepository
from app.service.orderitem_service import OrderItemService

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

def get_cartitem_service(db=Depends(get_db)):
    cartitem_repository = CartItemRepository(db)
    cartitem_service = CartItemService(cartitem_repository)
    return cartitem_service

def get_order_service(db=Depends(get_db)):
    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)
    return order_service

def get_orderitem_service(db=Depends(get_db)):
    orderitem_repository = OrderItemRepository(db)
    orderitem_service = OrderItemService(orderitem_repository)
    return orderitem_service