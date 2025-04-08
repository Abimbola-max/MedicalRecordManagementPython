from dataclasses import dataclass


@dataclass
class UserRegistrationDTO:
    username: str
    email: str
    password: str
    role: str