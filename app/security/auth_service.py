import datetime
from datetime import timezone

from fastapi import HTTPException,status
import jwt
from app.core.logger_config import logging

SECRET_KEY = 'sonali123'
ALGORITHM = 'HS256'

def verify_access_token(self,token):
    auth=AuthContext
    payload = decode_token(token)
    user = self.user_repo.get_user_by_id(payload["user_id"])
    
    if not user:
        raise UserNotFound()
    
    auth = AuthContext(
        user_id = user.id,
        permissions=permissions,
    )
    
    raise verify_access_token