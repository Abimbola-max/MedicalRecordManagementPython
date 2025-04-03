from abc import ABC, abstractmethod

from src.data.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def count_users(self):
        pass

    @abstractmethod
    def find_user_by(self, email: str):
        pass





    # all repositories methods like save, find, etc