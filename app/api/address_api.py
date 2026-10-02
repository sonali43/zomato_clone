from fastapi import APIRouter,Depends
from app.schema.address_schema import AddressSchema,UpdateAddress,AddressResponse
from app.dependency.service_dependency import get_address_service
from app.service.address_service import AddressService
from app.db.database import get_db
from sqlalchemy.orm import Session

address_router=APIRouter(prefix="/address",tags=["address"])

@address_router.post("/create_address",response_model="AddressResponse")
def create_address(create_address:AddressSchema,service:AddressService=Depends(get_address_service)):
    return service.create_address(create_address)

# @address_router.get("/get-address-by-id",response_model="AddressResponse")
# def get_address_by_id(get_address_by_id:AddressSchema,service:AddressService=Depends(get_address_service)):
#     return service.get_address_by_id(get_address_by_id)

# @address_router.get("/get-address-by-user-id",response_model="AddressResponse")
# def get_address_by_user_id(get_address_by_user_id:AddressSchema,service:AddressService=Depends(get_address_service)):
#     return service.get_address_by_user_id(get_address_by_user_id)

