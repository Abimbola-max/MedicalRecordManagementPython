from abc import ABC, abstractmethod

from src.data.models.doctorprofile import DoctorProfile


class Doctors(ABC):

    @abstractmethod
    def save_doctor(self, doctor: DoctorProfile):
        pass

    @abstractmethod
    def get_available_doctors(self):
        pass

    @abstractmethod
    def update_doctor_availability(self, doctor_email: str, available:bool):
        pass

    @abstractmethod
    def count(self):
        pass

    def find_by_id(self, doctor_id):
        pass