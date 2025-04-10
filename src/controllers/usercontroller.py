from flask import request, jsonify

from src.exceptions.exceptions import *
from src.services.usersauthentication.userservices import UserServices


class UserController:

    def __init__(self, user_service: UserServices):
        self.user_service = user_service

    def register(self):
        try:
            data = request.get_json()
            if not data or not all(key in data for key in ['username', 'email', 'password']):
                return jsonify({"error": "Missing required fields"}), 400

            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            roles = data.get("roles", ["PATIENT"])

            if isinstance(roles, str):
                roles = [roles]

            user_id = self.user_service.register_user(
                username=username,
                email=email,
                password=password,
                roles=roles
            )

            return jsonify({
                "message": "User registered successfully",
                "user_id": str(user_id),
                "roles": roles
            }), 201

        except EmailAlreadyExistException as e:
            return jsonify({"error": str(e)}), 409
        except InvalidRoleException as e:
            return jsonify({"error": str(e)}), 400
        except ErrorRegistering as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    def login(self):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return jsonify({"error": "Email and password required"}), 400

            credentials = self.user_service.login(email, password)
            return jsonify(credentials), 200

        except NotFoundException as e:
            return jsonify({"error": str(e)}), 404
        except IncorrectPasswordException as e:
            return jsonify({"error": str(e)}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500

