from app.repo.address_repo import AddressRepository
from app.schema.address_schema import AddressSchema, UpdateAddress
from sqlalchemy.orm import Session


class AddressService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.address_repo = AddressRepository(db_session)

    def create_address_service(self, create_address:AddressSchema):
        return self.address_repo.create_address_repo(create_address)

    def get_address_by_id_service(self, address_id: int):
        address = self.address_repo.get_address_by_id(address_id)

        if address is None:
            raise ValueError("Address not found")
        return address

    def get_address_by_user_id_service(self, user_id: int):
        return self.address_repo.get_address_by_user_id(user_id)

    def update_address_service(self,address_id: int,update_address: UpdateAddress):
        address = self.address_repo.get_address_by_id(address_id)

        if address is None:
            raise ValueError("Address not found")

        return self.address_repo.update_address(address,update_address)

    def delete_address_service(self, address_id: int):
        address = self.address_repo.get_address_by_id(address_id)

        if address is None:
            raise ValueError("Address not found")

        self.address_repo.delete_address(address)
        return {"message": "Address deleted successfully"}