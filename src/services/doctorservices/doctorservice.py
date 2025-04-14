from typing import List

from src.data.models.doctorprofile import DoctorProfile
from src.data.repositories.doctorrepositories.doctorrepository import DoctorRepository
from src.data.repositories.userrepositories.users import Users


class DoctorService:

    def __init__(self, doctor_repo: DoctorRepository):
        self.doctor_repo = doctor_repo


    def get_available_doctors(self) -> List[DoctorProfile]:
        return self.doctor_repo.get_available_doctors()