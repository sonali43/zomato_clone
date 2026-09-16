from pydantic import BaseModel, EmailStr

class CreateRestaurantRequest(BaseModel):
    name: str
    location: str
    address :str
    email: EmailStr
    phone: str
    
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
        