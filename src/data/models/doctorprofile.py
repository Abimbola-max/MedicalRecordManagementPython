from src.data.models.gender import Gender
from src.data.models.role import Role
from src.data.models.specialization import Specialization
from src.data.models.user import User


class DoctorProfile(User):

    def __init__(self, username, email, password, first_name, last_name, phone_number, gender, specialization:Specialization, user_id):
        super().__init__(username, email, password, [Role.DOCTOR])
        self.doctor_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.specialization = specialization
        self.gender = gender
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
        try:
            self.__specialization = Specialization(value)
        except ValueError as e:
            raise ValueError(str(e))

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        try:
            self.__gender = Gender(gender)
        except ValueError as e:
            raise ValueError(str(e))

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, value):
        self.__is_available = value



