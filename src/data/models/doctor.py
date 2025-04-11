from src.data.models.role import Role
from src.data.models.specialization import Specialization
from src.data.models.user import User


class Doctor(User):

    def __init__(self, username, email, password, first_name, last_name, phone_number, specialization:Specialization, user_id =None):
        super().__init__(username, email, password, [Role.DOCTOR])
        self.doctor_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.specialization = specialization
        self.is_available = True

    @property
    def doctor_id(self):
        return self.__doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self.__doctor_id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, number):
        self.__phone_number = number

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        self.__specialization = value



