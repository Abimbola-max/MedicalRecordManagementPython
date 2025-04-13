from src.data.models.appointment import Appointment


class AdminService:

    def __init__(self, doctor_service, patient_service, appointment_service):
        self.doctor_service = doctor_service
        self.patient_service = patient_service
        self.appointment_service = appointment_service

    def schedule_appointment(self, patient_id, doctor_id, date_time):
        appointment_data = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time
        )
        return self.appointment_service.create_appointment(appointment_data)











































































































    # def generate_report(self):
    #     appointments = self.appointment_service.get_appointments()
    #
    #     report = []
    #     for appointment in appointments:
    #         report.append({
    #             "date_time": appointment.date.strftime("%Y-%m-%d %H:%M:%S"),
    #             "patient": f"{appointment.patient.first_name} {appointment.patient.last_name}",
    #             "doctor": f"Dr. {appointment.doctor.first_name} {appointment.doctor.last_name}",
    #             "specialization": appointment.doctor.specialization.value,
    #         })
    #
    #     return report