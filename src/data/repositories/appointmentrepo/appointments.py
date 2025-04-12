from abc import ABC, abstractmethod

from src.data.models.appointment import Appointment


class Appointments(ABC):

    @abstractmethod
    def create_appointment(self, appointment: Appointment):
        pass

    @abstractmethod
    def get_all_appointment(self):
        pass