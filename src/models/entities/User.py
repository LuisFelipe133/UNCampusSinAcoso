from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    rol:str

    def __init__(self, id, correo, password) -> None:
        self.id = id
        self.correo = correo
        self.password = password
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    @classmethod
    def createPassword(self,password_to_be_hashed:str)->str:
        return generate_password_hash(password_to_be_hashed)
    
    @classmethod
    def setUserRol(self,role:str):
        self.rol = role
    
    @classmethod
    def getUserRol(self)->str:
        return self.rol

