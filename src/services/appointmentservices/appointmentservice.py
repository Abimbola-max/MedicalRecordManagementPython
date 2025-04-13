from src.data.models.appointment import Appointment
from src.data.repositories.appointmentrepo.appointmentrepository import AppointmentRepository
from src.data.repositories.appointmentrepo.appointments import Appointments
from src.data.repositories.doctorrepositories.doctorrepository import DoctorRepository
from src.data.repositories.patientrepositories.patients import Patients
from src.data.repositories.userrepositories.users import Users
from src.exceptions.exceptions import NotFoundException


class AppointmentService:

    def __init__(self, appointment_repo: AppointmentRepository, patient_repo: Patients, doctor_repo: DoctorRepository):
        self.appointment_repo = appointment_repo
        self.patient_repo = patient_repo
        self.doctor_repo = doctor_repo

    def create_appointment(self, patient_id, doctor_id, date_time):
        patient = self.patient_repo.find_by_id(patient_id)
        doctor = self.doctor_repo.find_by_id(doctor_id)

        if not patient:
            raise NotFoundException(f"Patient with id {patient_id} not found")
        if not doctor:
            raise NotFoundException(f"Doctor with id {doctor_id} not found")

        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time
        )
        appointment_id = self.appointment_repo.save(appointment)
        return appointment_id

    def is_doctor_available(self, doctor_id, date_time):
        appointments = self.appointment_repo.find_by_doctor_id(doctor_id)

        for appointment in appointments:
            if appointment.date_time == date_time:
                return False
        return True