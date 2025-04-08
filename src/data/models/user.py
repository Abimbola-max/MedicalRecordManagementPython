from abc import ABC, abstractmethod

from src.data.models.passwordencrypt import PasswordEncrypt
from src.data.models.validator import Validator


class User(ABC):


    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = PasswordEncrypt.encrypt_password(password)
        self.role = role

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        Validator.validate_first_name(username)
        self.__username = username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        Validator.validate_email(email)
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        Validator.validate_password(password)
        self.__password = password

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role


