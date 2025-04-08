from src.data.models.passwordencrypt import PasswordEncrypt
from src.data.models.role import Role
from src.data.models.user import User
from src.data.models.validator import Validator
from src.data.repositories.userrepository import UserRepository
from src.exceptions.exceptions import *


class UserServices:

    def __init__(self, user_repo: UserRepository):
        self.repository = user_repo
        self.password_encrypt = PasswordEncrypt()

    def register_user(self, username, email, password, role):
        try:
            Validator.validate_first_name(username)
            Validator.validate_email(email)
            Validator.validate_password(password)
        except InvalidEmailPatternException as e:
            print(e)
        except InvalidNameException as e:
            print(f"Error {e}")
        except InvalidRoleException as e:
            raise InvalidRoleException(f"Invalid role {role}. Must either be Doctor, Patient or Admin")

        existing_user = self.repository.find_user_by(email)
        if existing_user == True:
            raise EmailAlreadyExistException(f"User with email {email} already exist.")

        new_user = User(username.strip(), email.strip(), password.strip(), role)
        user_id = self.repository.save_user(new_user)
        return user_id

    def login(self, email, password):
        user_data = self.repository.find_user_by(email)

        if not user_data:
            raise NotFoundException(f"User with email {email} not found.")

        user_password = user_data.get('password')
        if not PasswordEncrypt.verify_password(user_password, password.strip()):
            raise IncorrectPasswordException("Incorrect password.")
        return {"message": "Login successful", "user_id": str(user_data.get('_id'))}



































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