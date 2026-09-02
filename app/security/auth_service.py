from app.core.auth_cntx import AuthContext
from app.security.tokenHandel import generate_token,decode_auth_token
from app.repo.user_repo import UserRepository
from app.custom_exception.custom_exception import UserNotFoundException

class AuthService:
    
    def __init__(self,user_repo:UserRepository):
        self.user_repo : UserRepository = user_repo
        
    def create_user_token(self,user_email,password):
        
        user = self.user_repo.get_user_by_email(user_email)
        if user is None:
            raise UserNotFoundException("Enter a vaild email address")
        if user.password is None:
            raise ValueError("User has no password")
        if user.password != password:
            raise UserNotFoundException("Enter a vaild password")
        user_auth_token = generate_token(user_id=user.id)
        return user_auth_token
        
    def verify_user_token(self,token):
        decode_token=decode_auth_token(token)
        user=self.user_repo.get_user_by_id(decode_token["user_id"])
        if user is None:
            raise UserNotFoundException("User doesn't found")
        auth_cntx=AuthContext(user_id=user.id)
        return auth_cntx
        


