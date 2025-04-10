from bson import ObjectId
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
            'roles': user.roles,
        }
        insert_document = self.collection.insert_one(user_data)
        default_return_mongo_id = insert_document.inserted_id
        return user_data

    def count_users(self):
        return self.collection.count_documents({})

    def find_user_by(self, email: str):
        user_data = self.collection.find_one({'email': email})
        if user_data:
            return User (
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'].strip(),
                roles=user_data.get('roles', []),
                _id=user_data.get('_id')
            )
        return None

    def find_user_by_both(self, email: str, roles: list):
        user_data = self.collection.find_one({'email': email, 'roles': {'$all': roles}})
        if user_data:
            return User (
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                roles=user_data.get('roles', [])
            )
        return None

    def find_user_by_id(self, user_id: str):
        return self.collection.find_one({'_id': ObjectId(user_id)})

    def close_client(self):
        self.client.close()




