from src.data.models.role import Role
from src.data.models.user import User


class Admin(User):

    def __init__(self, username:str, email: str, password: str):
        super().__init__(username, email, password, [Role.ADMIN])

