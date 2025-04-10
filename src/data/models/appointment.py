from datetime import datetime

from src.data.models.doctor import Doctor
from src.data.models.patientprofile import PatientProfile


class Appointment:

    def __init__(self, patient: PatientProfile, doctor: Doctor, date_time: datetime, reason: str = None):
        # self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
        self.reason = reason
        self.status = "scheduled"

    @property
    def patient(self):
        return self.__patient

    @patient.setter
    def patient(self, patient):
        self.__patient = patient

    @property
    def doctor(self):
        return self.__doctor

    @doctor.setter
    def doctor(self, dokita):
        self.__doctor = dokita

    @property
    def date_time(self):
        return self.__date_time

    @date_time.setter
    def date_time(self, date_time):
        self.__date_time = date_time.now()

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, reasons):
        self.__reason = reasons


    