from abc import ABC, abstractmethod

from src.data.models.patientprofile import PatientProfile


class PatientI(ABC):

    @abstractmethod
    def save_patient(self, patient: PatientProfile):
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def find_by_id(self, patient_id):
        pass

    @abstractmethod
    def book_appointment(self, patient_id, appointment_date, appointment_time, reason):
        pass