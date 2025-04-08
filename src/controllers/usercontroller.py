from flask import request

from src.services.authentication.userservices import UserServices


class UserController:

    def __init__(self, user_service: UserServices):
        self.user_service = user_service

    def register(self):
        try:
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            role = data.get("role", "user")
            user_id = self.user_service.register_user(username, email, password, role)
            return {"message": "User registered successfully", "user_id": str(user_id)}, 201
        except ValueError as e:
            return {"error": str(e)}, 400