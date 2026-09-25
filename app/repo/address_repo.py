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
        
    def get_address_by_id(self,address_id:int):
        address=self.db_session.query(Address).filter(Address.id==address_id).first()
        return address
    
    def get_address_by_user_id(self,user_id:int):
        address=self.db_session.query(Address).filter(Address.user_id==user_id).all()
        return address
    
    def update_address(self,address:Address,update_address:UpdateAddress):
        if update_address.house_no is not None:
            address.house_no= update_address.house_no  
        if update_address.street is not None:
            address.street = update_address.street
        if update_address.city is not None:
            address.city = update_address.city
        if update_address.state is not None:
            address.state = update_address.state
        if update_address.pincode is not None:
            address.pincode = update_address.pincode
        if update_address.landmark is not None:
            address.landmark = update_address.landmark
        if update_address.address_type is not None:
            address.address_type = update_address.address_type
            
        try:
            self.db_session.commit()
            self.db_session.refresh(address)
            return address
        except Exception as e:
            self.db_session.rollback()
            raise ValueError(str(e))
        
    def delete_address(self,address:Address):
        try:
            self.db_session.delete(address)
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            raise ValueError (str(e))