from datetime import datetime

from src.data.models.doctorprofile import DoctorProfile
from src.data.models.patientprofile import PatientProfile


class Appointment:

    def __init__(self, patient_id: PatientProfile, doctor_id: DoctorProfile, date_time: datetime, reason: str = None, appointment_id=None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date_time = date_time
        self.reason = reason
        self.status = "scheduled"

    @property
    def patient_id(self):
        return self.__patient

    @patient_id.setter
    def patient_id(self, patient):
        self.__patient = patient

    @property
    def appointment_id(self):
        return self.__appointment_id

    @appointment_id.setter
    def appointment_id(self, appointment):
        self.__appointment_id = appointment

    @property
    def doctor_id(self):
        return self.__doctor

    @doctor_id.setter
    def doctor_id(self, dokita):
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

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status


    