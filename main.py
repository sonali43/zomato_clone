from fastapi import FastAPI
from fastapi.routing import APIRoute
from app.db.database import get_db, Base, engine
from app.model.user_model import User
from app.model.food_model import Food
from app.api.user_api import user_router
from app.api.restaurant_router import router as restaurant_router

app = FastAPI()

app.include_router(user_router)
app.include_router(restaurant_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"Hii sonali"}