from dataclasses import dataclass


@dataclass
class AuthResponseDTO:
    message: str
    user_id: str = None
    access_token: str = None