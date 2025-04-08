from src.exceptions.exceptions import NotAlistException


class MedicalHistory:

    def __init__(self):
        self.allergies = []
        self.surgeries = []

    @property
    def allergies(self):
        return self.__allergies

    @allergies.setter
    def allergies(self, value):
        if not isinstance(value, list):
            raise NotAlistException("Not a list.")
        self.__allergies = value

    @property
    def surgeries(self):
        return self.__surgeries

    @surgeries.setter
    def surgeries(self, value):
        if not isinstance(value, list):
            raise NotAlistException("Not a list.")
        self.__surgeries = value
