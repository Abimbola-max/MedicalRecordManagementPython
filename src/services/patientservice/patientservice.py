from src.data.models import user
from src.data.models.patientprofile import PatientProfile
from src.data.models.role import Role
from src.data.repositories.patientrepo.patients import Patients
from src.data.repositories.users import Users
from src.exceptions.exceptions import UserDoesNotExistException


class PatientService:

    def __init__(self, patient_repo: Patients, user_repo: Users):
        self.patient_repo = patient_repo
        self.user_repo = user_repo

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
        return self.patient_repo.save_patient(patient)