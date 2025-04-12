from typing import List

from pymongo import MongoClient

from src.data.models.doctorprofile import DoctorProfile
from src.data.models.gender import Gender
from src.data.models.role import Role
from src.data.models.specialization import Specialization
from src.data.repositories.doctorrepositories.doctors import Doctors
from src.data.repositories.userrepositories.users import Users
from src.exceptions.exceptions import UserDoesNotExistException, NotFoundException


class DoctorRepository(Doctors):

    def __init__(self, doctor_repo: Users):
        self.user = doctor_repo
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['medical_report_management_system']
        self.collection = self.database['doctors']
        # self.appointments_collection = self.database['appointments']

    def save_doctor(self, doctor: DoctorProfile):
        user_data = self.user.find_user_by_id(doctor.doctor_id)
        if not user_data:
            raise UserDoesNotExistException("User does not exist.")

        doctor_data = {
            'user_id': str(doctor.doctor_id),
            'first_name': doctor.first_name,
            'last_name': doctor.last_name,
            'email': doctor.email,
            'phone_number': doctor.phone_number,
            'gender': doctor.gender.value,
            'specialization': doctor.specialization.value
        }
        insert_document = self.collection.insert_one(doctor_data)
        default_return_mongo_id = insert_document.inserted_id
        return str(default_return_mongo_id)

    def get_available_doctors(self) -> List[DoctorProfile]:
        return [DoctorRepository.__doc_to_doctor(doc) for doc in self.collection.find({'is_available': True})]

    def update_doctor_availability(self, doctor_email: str, available:bool):
        self.collection.update_one(
            {'email': doctor_email},
            {'$set': {'is_available': available}},
        )

    @staticmethod
    def __doc_to_doctor(doc) -> DoctorProfile:
        return DoctorProfile(
            username=doc['username'],
            email=doc['email'],
            password=doc['password'],
            first_name=doc['first_name'],
            last_name=doc['last_name'],
            phone_number=doc['phone_number'],
            gender=Gender(doc['gender']),
            specialization=Specialization(doc['specialization'])
        )

    def count(self):
        return self.collection.count_documents({})

    def find_by_id(self, doctor_id):
        doctor_data = self.collection.find_one({'doctor_id': doctor_id})
        if not doctor_data:
            raise NotFoundException("doctor not Found.")
        user_data = self.user.find_user_by_id(doctor_data['doctor_id'])
        if not user_data:
            raise NotFoundException("User not found.")

        user_data.pop('password', None)

        return {
            **doctor_data,
            **user_data,
            'roles': [Role(role) for role in user_data.get('roles')],
        }