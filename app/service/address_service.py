
from app.repo.address_repo import AddressRepository
from app.schema.address_schema import AddressSchema, UpdateAddress


class AddressService:
    def __init__(self, address_repo: AddressRepository):
        self.address_repo: AddressRepository = address_repo

    def create_address_service(self, create_address: AddressSchema):
        return self.address_repo.create_address_repo(create_address)

    def get_address_by_id(self, address_id: int):
        return self.address_repo.get_address_by_id(address_id)

    def get_address_by_user_id(self, user_id: int):
        return self.address_repo.get_address_by_user_id(user_id)

    def update_address(self, address_id: int, update_address: UpdateAddress):
        address = self.address_repo.get_address_by_id(address_id)

        if address is None:
            raise ValueError("Address not found")
        return self.address_repo.update_address(address, update_address)

    def delete_address(self, address_id: int):
        address = self.address_repo.get_address_by_id(address_id)

        if address is None:
            raise ValueError("Address not found")
        self.address_repo.delete_address(address)
        return {"Address deleted successfully"}
