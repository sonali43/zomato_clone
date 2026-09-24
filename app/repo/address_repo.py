from sqlalchemy.orm import Session
from app.model.address_model import Address
from app.schema.address_schema import AddressSchema,UpdateAddress

class AddressRepository:
    def __init__ (self,db_session:Session):
        self.db_session=db_session
        
    def create_address_repo(self,create_address:AddressSchema):
        address=Address(
            user_id=create_address.user_id,
            house_no=create_address.house_no,
            street=create_address.street,
            city=create_address.city,
            state=create_address.state,
            pincode=create_address.pincode,
            landmark=create_address.landmark,
            address_type=create_address.address_type
        )
        
        try:
            self.db_session.add(address)
            self.db_session.commit()
            self.db_session.refresh(address)
            return address
        except Exception as e:
            self.db_session.rollback()
            raise ValueError(str(e))
        
    def get_aadress_by_id(self,address_id:int):
        address=self.db_session.query(Address).filter(Address.id==address_id).first()
        return address
    
    def get_address_by_user_id(self,user_id:int):
        address=self.db_session.query(Address).filter(Address.user_id==user_id).all()
        return address
    
    def update_address(self,address_id:int,address:UpdateAddress):
        existing_address=self.db_session.query(Address).filter(Address.id==address_id).first()
        if existing_address is None:
            return None
        if existing_address is not None:
            