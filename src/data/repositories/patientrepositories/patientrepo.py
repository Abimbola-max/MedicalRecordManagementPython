from abc import ABC, abstractmethod
from typing import Optional

from src.data.models.patientprofile import PatientProfile


class PatientRepo(ABC):

    @abstractmethod
    def save(self, patient: PatientProfile):
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def find_by_id(self, patient_id):
        pass

    @abstractmethod
    def find_profile(self, user_id: str)-> Optional[PatientProfile]:
        pass

    @abstractmethod
    def book_appointment(self, patient_id, appointment_date, appointment_time, reason):
        pass