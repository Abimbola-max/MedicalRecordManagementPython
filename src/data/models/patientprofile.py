from datetime import datetime

from src.data.models.gender import Gender
from src.data.models.role import Role
from src.data.models.user import User


class PatientProfile(User):

    def __init__(self, username, email, password, user_id: str, first_name: str, last_name: str, date_of_birth, phone_number: str, gender: str, medical_history: str):
        super().__init__(username, email, password, [Role.PATIENT])
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        # self.gender = gender
        self.medical_history = medical_history
        try:
            # Pass gender directly to the Gender enum (case-insensitive)
            self.gender = Gender(gender)
        except ValueError as e:
            raise ValueError(str(e))

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, number):
        self.__phone_number = number

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def medical_history(self):
        return self.__medical_history

    @medical_history.setter
    def medical_history(self, value):
        self.__medical_history = value

    def update_medical_history(self, new_medical_history):
        self.medical_history = new_medical_history

    @property
    def get_age(self) -> int:
        today_date = datetime.now().date()
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()

        actual_year = today_date.year - birth_date.year
        actual_month = today_date.month - birth_date.month
        actual_day = today_date.day - birth_date.day

        if actual_month < 0 or (actual_month == 0 and actual_day < 0):
            actual_year -= 1
        return actual_year

