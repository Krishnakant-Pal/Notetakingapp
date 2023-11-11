# from  website import mongo
from website.config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, email= None):
        
        self.email = email
    

    def create_user(self, username, email, password):
        hashed_password = generate_password_hash(password)
        db.users.insert_one({'username': username, 'email': email, 'password': hashed_password})

    def find_user(self, email):
        return db.users.find_one({'email': email})

    def check_password(self, password):
        user = db.users.find_one({"email": self.email})
        return check_password_hash(user['password'], password)
    
    def get_id(self):
        return self.email