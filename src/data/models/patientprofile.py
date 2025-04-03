from datetime import datetime

from src.data.models.user import User


class PatientProfile(User):

    def __init__(self, username, email, password, role, user_id: str, first_name: str, last_name: str, date_of_birth, phone_number: str, medical_history: str):
        super().__init__(username, email, password, role)
        self.patient_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.medical_history = medical_history

    @property
    def patient_id(self):
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, value):
        self.__patient_id = value

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

    def update_medical_history(self, new_medical_history):
        self.medical_history = new_medical_history

    def get_actual_age(self) -> int:
        today_date = datetime.now().date()
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()

        actual_year = today_date.year - birth_date.year
        actual_month = today_date.month - birth_date.month
        actual_day = today_date.day - birth_date.day

        if actual_month < 0 or (actual_month == 0 and actual_day < 0):
            actual_year -= 1
        return actual_year

    def view_profile(self):
        return {
            'patient_id': self.patient_id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.get_actual_age(),
            'email': self.email,
            'phone_number': self.phone_number,
            'medical_history': self.medical_history
        }

