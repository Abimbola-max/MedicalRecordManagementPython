from abc import ABC, abstractmethod

from src.data.models.appointment import Appointment


class Appointments(ABC):

    @abstractmethod
    def save(self, appointment: Appointment):
        pass

    @abstractmethod
    def get_all_appointment(self):
        pass

    @abstractmethod
    def find_by_id(self, user_id):
        pass

    @abstractmethod
    def find_by_doctor_id(self, doctor_id):
        pass