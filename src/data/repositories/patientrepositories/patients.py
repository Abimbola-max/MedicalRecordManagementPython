from typing import Optional

from pymongo import MongoClient

from src.data.models.gender import Gender
from src.data.models.patientprofile import PatientProfile
from src.data.repositories.patientrepositories.patientrepo import PatientRepo
from src.data.repositories.userrepositories.users import Users
from src.exceptions.exceptions import UserDoesNotExistException, NotFoundException


class Patients(PatientRepo):

    def __init__(self, user_repo: Users):
        self.users = user_repo
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['medical_report_management_system']
        self.collection = self.database['patients']
        self.appointments_collection = self.database['appointments']

    def save(self, patient: PatientProfile):
        user_data = self.users.find_user_by_id(patient.user_id)
        if not user_data:
            raise UserDoesNotExistException("User does not exist.")

        patient_data = {
            'user_id': str(patient.user_id),
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'email': patient.email,
            'date_of_birth': patient.date_of_birth,
            'phone_number': patient.phone_number,
            'gender': patient.gender.value,
            'medical_history': patient.medical_history
        }
        insert_document = self.collection.insert_one(patient_data)
        default_return_mongo_id = insert_document.inserted_id
        return str(default_return_mongo_id)

    def count(self):
        return self.collection.count_documents({})

    def find_by_id(self, patient_id: str):
        patient_data = self.collection.find_one({'patient_id': patient_id})
        if not patient_data:
            raise NotFoundException("Patient not Found.")
        user_data = self.users.find_user_by_id(patient_data['patient_id'])
        if not user_data:
            raise NotFoundException("User not found.")

        user_data.pop('password', None)

        return {
            **patient_data,
            **user_data
            # 'roles': [Role(role) for role in user_data.get('roles')],
        }

    def find_profile(self, user_id: str) -> Optional[PatientProfile]:
        data = self.collection.find_one({'user_id': user_id})
        if not data:
            raise NotFoundException("Patient not found.")
        else:
            user_data = self.collection.find_one({'_id': user_id})
            return PatientProfile(
                user_id=user_data['-id'],
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                date_of_birth=data['date_of_birth'],
                phone_number=data['phone_number'],
                gender=data['gender'],
                medical_history=data['medical_history']
            )


    def book_appointment(self, patient_id, appointment_date, appointment_time, reason):
        patient = self.collection.find_one({'patient_id': patient_id})
        if not patient:
            print(f"Patient with ID {patient_id} not found.")
            return None

        new_appointment = {
            'patient_id': patient_id,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time,
            'reason': reason
        }
        insert_result = self.appointments_collection.insert_one(new_appointment)
        return insert_result.inserted_id






