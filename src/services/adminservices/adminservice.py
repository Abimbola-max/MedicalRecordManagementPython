from src.data.models.appointment import Appointment


class AdminService:

    def __init__(self, user_service, doctor_service, patient_service, appointment_service):
        self.user_service = user_service
        self.doctor_service = doctor_service
        self.patient_service = patient_service
        self.appointment_service = appointment_service

    def schedule_appointment(self, patient_id: str, doctor_id: str, date_time):
        appointment_data = Appointment(
            patient_id= ',
            doctor_id=doctor_id,
            date_time=date_time
        )