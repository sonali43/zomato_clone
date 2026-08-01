from sqlalchemy.orm import Session
from app.repo.user_repo import user_repo
from app.model.user_model import User as Users

class UserService:
    
    
    def create_user(self,id: int, username: str, email:str, age: int, db: Session):
        user = Users(id=id, username=username,email=email, age=age)
        return user_repo.created_user(user,db_session=db)
    
    
    
    
    
user_service = UserService()