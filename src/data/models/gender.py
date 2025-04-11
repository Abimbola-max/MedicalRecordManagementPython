from enum import Enum


class Gender(Enum):

    FEMALE = "female"
    MALE = "male"

    @classmethod
    def _missing_(cls, value):
        # Normalize input to lowercase for case-insensitive matching
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"Invalid gender: {value}. Must be one of: {[m.value for m in cls]}")