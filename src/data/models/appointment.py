from src.data.models.patient import Patient


class Appointment:

    def __init__(self, appointment_id: int, patient: Patient, doctor: Doctor, date: datetime, time: str, reason: str = None):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.reason = reason