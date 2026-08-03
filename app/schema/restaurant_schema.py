from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateRestaurantRequest(BaseModel):
    name: str
    location: str
    email: EmailStr
    
class RestaurantResponse(BaseModel):
    name: str
    location :str
    email:str
    rating : int | None
    
    class Config:
        orm_mode =True
        
        
class RestaurantListResponse(BaseModel):
    restaurants : list[RestaurantResponse]
    
    class Config:
        orm_mode =True
        