from src.data.models.patientprofile import PatientProfile
from src.data.models.role import Role
from src.data.repositories.patientrepositories.patients import PatientRepo
from src.data.repositories.userrepositories.users import Users
from src.exceptions.exceptions import UserDoesNotExistException


class PatientService:

    def __init__(self, patient_repo: PatientRepo, user_repo: Users, appointment_service):
        self.patient_repo = patient_repo
        self.user_repo = user_repo
        self.appointment_service  = appointment_service

    def create_patient_profile(self, user_id:str, profile: dict):
        user_check = self.user_repo.find_user_by_id(user_id)
        if not user_check:
            raise UserDoesNotExistException("User does not exist.")

        if Role.PATIENT.value not in user_check.get('roles', []):
            raise UserDoesNotExistException("User is not a patient.")

        patient = PatientProfile (
            username=user_check['username'],
            email=user_check['email'],
            password=user_check['password'],
            user_id=user_id,
            **profile
        )
        return self.patient_repo.save(patient)

    def book_appointment(self, patient_id, doctor_id, date_time, reason):
        patient = self.patient_repo.find_by_id(patient_id)
        doctor = self.appointment_service.doctor_service.find_by_id(doctor_id)
