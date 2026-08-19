import datetime
from datetime import timezone

from fastapi import HTTPException,status
import jwt
from app.core.logger_config import logger

SECRET_KEY = 'sonali'
ALGORITHM = 'HS256'

def generate_token(user_id :int):
    user_id = str(user_id)
    payload = {
        "user_id" : user_id,
        "exp":datetime.datetime.now(timezone.utc) + datetime.timedelta(minutes=60),
    }
    
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    logger.info(f"user with {user_id} has this {token}")
    return token

def decode_auth_token(auth_token : str):
    try:
        payload = jwt.decode(auth_token,
                             SECRET_KEY,
                             algorithms=ALGORITHM)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    logger.info(f"user with {auth_token} has this {payload}")
    return payload