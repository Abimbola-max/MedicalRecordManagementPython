from dataclasses import dataclass


@dataclass
class UserLoginDTO:
    email: str
    password: str