from enum import Enum


class Role(Enum):

    ADMIN = 'ADMIN'
    PATIENT = 'PATIENT'
    DOCTOR = 'DOCTOR'

    @classmethod
    def is_valid(cls, role):
        return role in {item.value for item in cls}