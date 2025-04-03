from pymongo import MongoClient

from src.data.models.user import User
from src.data.repositories.userrepository import UserRepository


class Users(UserRepository):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['medical_report_management_system']
        self.collection = self.database['users']


    def save_user(self, user: User):
        user_data = {
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'role': user.role.value,
            # 'profile': user.profile
        }
        insert_document = self.collection.insert_one(user_data)
        default_return_mongo_id = insert_document.inserted_id
        return default_return_mongo_id

    def count_users(self):
        return self.collection.count_documents({})

    def find_user_by(self, email: str):
        return self.collection.find_one({'email': email})




