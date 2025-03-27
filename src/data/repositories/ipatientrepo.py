from abc import ABC, abstractmethod

from src.data.models.patient import Patient


class PatientI(ABC):

    # @abstractmethod
    # def book(self, appointment: Appointment):
    #     pass

    @abstractmethod
    def save(self, patient: Patient):
        pass

    @abstractmethod
    def count(self):
        pass