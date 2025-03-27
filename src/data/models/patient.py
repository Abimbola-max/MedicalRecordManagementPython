from datetime import datetime

class Patient:

    def __init__(self, patient_id: str, first_name: str, last_name: str, email: str, date_of_birth, phone_number: str, medical_history: str):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth


        # if isinstance(date_of_birth, str):
        #     self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").strftime("%Y-%m-%d")
        # else:
        #     self.date_of_birth = date_of_birth.strftime("%Y-%m-%d")
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

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email