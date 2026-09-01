from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from app.db.database import get_db, Base, engine
from app.model.user_model import User
from app.model.food_model import Food
from app.api.user_api import user_router
from app.api.restaurant_router import router as restaurant_router
from app.api.food_api import food_router
from app.api.cart_api import cart_router
from app.api.cartitem_api import cartitem_router
from app.api.order_api import order_router
from app.custom_exception.app_exception import AppException
from app.security.auth_dependency import auth_dependency
from fastapi.exceptions import RequestValidationError
from app.custom_exception.exception_handler import app_exception_handler,generic_exception_handler,validation_exception_handler


app = FastAPI()

app.include_router(user_router)
app.include_router(restaurant_router)
app.include_router(food_router,dependencies=[Depends(auth_dependency)])
app.include_router(cart_router)
app.include_router(cartitem_router)
app.include_router(order_router)
app.add_exception_handler(
    AppException,
    app_exception_handler
)
app.add_exception_handler(
    Exception,
    generic_exception_handler
)
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"Hii sonali"}