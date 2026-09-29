from fastapi import APIRouter,Depends
from app.schema.address_schema import AddressSchema,UpdateAddress,AddressResponse
from app.dependency.service_dependency import get_address_service
from app.service.address_service import AddressService
from app.db.database import get_db
from sqlalchemy.orm import Session

address_router=APIRouter(prefix="/address",tags=["address"])

@address_router.post("/create_address"response_model="AddressResponse")
def create_address(create_address:AddressSchema,service:AddressService=Depends(get_address_service)):
    return service.create_address(create_address)
