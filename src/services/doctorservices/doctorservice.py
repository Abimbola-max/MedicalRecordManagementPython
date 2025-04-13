from typing import List

from src.data.models.doctorprofile import DoctorProfile
from src.data.models.gender import Gender
from src.data.models.role import Role
from src.data.models.specialization import Specialization
from src.data.repositories.doctorrepositories.doctorrepository import DoctorRepository
from src.data.repositories.userrepositories.users import Users
from src.exceptions.exceptions import UserDoesNotExistException


class DoctorService:

    def __init__(self, doctor_repo: DoctorRepository, user_repo: Users):
        self.doctor_repo = doctor_repo
        self.user_repo = user_repo

    def get_available_doctors(self) -> List[DoctorProfile]:
        return self.doctor_repo.get_available_doctors()

    def create_doctor_profile(self, doctor_id:str, profile: dict):
        user_check = self.user_repo.find_user_by_id(doctor_id)
        if not user_check:
            raise UserDoesNotExistException("User does not exist.")

        if Role.DOCTOR.value not in user_check.get('roles', []):
            raise UserDoesNotExistException("User is not a doctor.")

        # try:
        #     specialization = Specialization(profile.get('specialization'))
        #     gender = Gender(profile.get('gender'))
        # except ValueError as e:
        #     raise ValueError(f"Invalid specialization or gender: {e}")

        doctor = DoctorProfile(
            username=user_check['username'],
            email=user_check['email'],
            password=user_check['password'],
            first_name=profile.get('first_name'),
            last_name=profile.get('last_name'),
            phone_number=profile.get('phone_number'),
            gender=profile.get('gender'),
            specialization=profile.get('specialization'),
            user_id=doctor_id
        )
        return self.doctor_repo.save_doctor(doctor)