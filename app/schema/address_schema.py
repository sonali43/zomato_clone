from pydantic import BaseModel

class AddressSchema(BaseModel):
    house_no:str
    street:str
    city:str
    state:str
    pincode: str
    landmark: str |None=None
    address_type:str |None=None
    
class UpdateAddress(BaseModel):
    house_no:str|None=None
    street:str|None=None
    city:str|None=None
    state:str|None=None
    pincode: str|None=None
    landmark: str |None=None
    address_type:str |None=None
    
class AddressResponse(BaseModel):
    id:int
    user_id:int
    house_no:str
    street:str
    city:str
    state:str
    pincode: str
    landmark: str |None=None
    address_type:str |None=None
    
class Config:
    from_attributes=True
    