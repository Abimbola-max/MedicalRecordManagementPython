from abc import ABC

from src.data.models.passwordencrypt import PasswordEncrypt
from src.data.models.role import Role
from src.data.models.validator import Validator


class User(ABC):


    def __init__(self, username: str, email: str, password: str, roles: list, _id=None):
        self._id = _id
        self.username = username
        self.email = email
        self.password = password
        self.roles = roles

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
        self.__password = password

    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, roles):
        self.__roles = roles

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    # @property
    # def another_role(self):
    #     return self.__another_role
    #
    # @another_role.setter
    # def another_role(self, another_role):
    #     self.__another_role = another_role
    #

