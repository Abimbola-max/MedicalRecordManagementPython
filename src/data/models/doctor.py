from src.data.models.role import Role
from src.data.models.specialization import Specialization
from src.data.models.user import User


class Doctor(User):

    def __init__(self, username, email, password, user_id, specialization:Specialization):
        super().__init__(username, email, password, Role.DOCTOR)
        self.doctor_id = user_id
        self.specialization = specialization
        self.schedule = {
            'monday': {'start': '09:00', 'end': '17:00'}
        }


    @property
    def doctor_id(self):
        return self.__doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self.__doctor_id = value

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        self.__specialization = value



