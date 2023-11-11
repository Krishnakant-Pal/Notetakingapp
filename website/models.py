# from  website import mongo
from website.config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def create_user(self, username, email, password):
        hashed_password = generate_password_hash(password)
        db.users.insert_one({'username': username, 'email': email, 'password': hashed_password})

    def find_user(self, email):
        return db.users.find_one({'email': email})

    def check_password(self, stored_password, password):
        return check_password_hash(stored_password, password)
