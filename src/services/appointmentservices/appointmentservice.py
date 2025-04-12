from src.data.repositories.appointmentrepo.appointmentrepository import AppointmentRepository
from src.data.repositories.appointmentrepo.appointments import Appointments
from src.data.repositories.userrepositories.users import Users


class AppointmentService:

    def __init__(self, appointment_repo: AppointmentRepository):
        self.appointment_repo = appointment_repo


