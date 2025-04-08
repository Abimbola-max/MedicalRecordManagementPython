from pymongo import MongoClient

from src.data.models.patientprofile import PatientProfile
from src.data.repositories.patientrepo import PatientI


class Patients(PatientI):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['medical_report_management_system']
        self.collection = self.database['patients']
        self.appointments_collection = self.database['appointments']

    def save_patient(self, patient: PatientProfile):
        new_patient_data = {'patient_id': patient.patient_id,
                       'first_name': patient.first_name,
                       'last_name': patient.last_name,
                       'email': patient.email,
                       'date_of_birth': patient.date_of_birth,
                       'phone_number': patient.phone_number,
                       'medical_history': patient.medical_history
                       }
        insert_document = self.collection.insert_one(new_patient_data)
        default_return_mongo_id = insert_document.inserted_id
        return default_return_mongo_id

    def count(self):
        return self.collection.count_documents({})

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


