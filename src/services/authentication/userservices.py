from src.data.models import user
from src.data.models.passwordencrypt import PasswordEncrypt
from src.data.models.role import Role
from src.data.models.user import User
from src.data.models.validator import Validator
from src.data.repositories.users import Users
from src.exceptions.exceptions import *


class UserServices:

    def __init__(self, user_repo: Users):
        self.repository = user_repo

    def register_user(self, username, email, password, roles):
        try:
            UserServices.__validate_register(username, email, password)

            if not isinstance(roles, (list, tuple)):
                roles = [roles]

            processed_roles = []
            for role in roles:
                if isinstance(role, Role):
                    processed_role = role.value.upper()
                else:
                    processed_role = str(role).upper()

                if not Role.is_valid(processed_role):
                    raise InvalidRoleException(f"Invalid role '{role}'. Must be one of: {Role.DOCTOR}, {Role.PATIENT}, {Role.ADMIN}")

                processed_roles.append(processed_role)

            password_hash = PasswordEncrypt.encrypt_password(password)

            existing_user = self.repository.find_user_by(email)
            if existing_user:
                raise EmailAlreadyExistException(f"User with email {email} already exists.")

            new_user = User(username.strip(), email.strip(), password_hash, processed_roles)
            user_id = self.repository.save_user(new_user)
            return user_id
        except InvalidNameException as e:
            print(f"Error {e}")
        except InvalidRoleException:
            raise InvalidRoleException(f"Invalid role {roles}. Must either be Doctor, Patient or Admin")


    def login(self, email, password):
        user_data = self.repository.find_user_by(email)

        if not user_data:
            raise NotFoundException(f"User with email {email} not found.")

        user_password = user_data.password
        print(f"Checking: {password!r} against {user_data.password!r}")

        if not PasswordEncrypt.verify_password(password, user_password):
            raise IncorrectPasswordException("Incorrect password.")
        return {
            "message": "Login successful",
            "user_id": str(user_data._id),
            "roles": user_data.roles,
            "email": user_data.email
        }

    @staticmethod
    def __validate_register(username, email, password):
        Validator.validate_first_name(username)
        Validator.validate_email(email)
        Validator.validate_password(password)


































    # def register(self, user: User):
    #     if self.repository.find_user_by(user.email):
    #         return False
    #
    #     user.password = self.password_encrypt.encrypt_password(user.password)
    #     self.repository.save_user(user)
    #     return True
    #
    # def login(self, email, password: str):
    #     user = self.repository.find_user_by(email)
    #     if user and self.password_encrypt.verify_password(password, user['password']):
    #         return self.__create_user_profile(user)
    #
    #     raise NotFoundException("User Not Found.")

    # @staticmethod
    # def __create_user_profile(user):
    #     patient_string = 'patient'
    #     if user['role'] == patient_string.lower():
    #         from src.data.models.patientprofile import PatientProfile
    #         return PatientProfile(
    #             username=user['username'],
    #             email=user['email'],
    #             password=user['password'],
    #             user_id=user['user_id'],
    #             first_name=user['first_name'],
    #             last_name=user['last_name'],
    #             date_of_birth=user['date_of_birth'],
    #             phone_number=user['phone_number'],
    #             gender = user['gender'],
    #             medical_history=user['medical_history']
    #         )

    # def view_profile(self, email):
    #     user = self.repository.find_user_by(email)
    #     if not user:
    #         raise NotFoundException("User Not Found.")
    #     if user['role'] == 'patient':
    #         patient = self.__create_user_profile(user)
    #         return patient.view_profile()
    #     elif user['role'] == 'doctor':
    #         doctor = self.__create_user_profile(user)
    #         return doctor.view_profile()
    #     raise ProfileDoesNotExistException("Profile does not exist.")