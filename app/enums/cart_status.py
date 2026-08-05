from enum import Enum

class CartStatus(str,Enum):
    SUCCESSFUL="successful"
    UNSUCCESSFUL="unsuccessful"
    CANCELLED="cancelled"