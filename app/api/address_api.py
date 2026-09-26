from fastapi import HTTPException,Depends
from app.schema.address_schema import AddressSchema,UpdateAddress,AddressResponse
from app.dependency.service_dependency import get_address_service
from app.db.database import get_db
from sqlalchemy.orm import Session
