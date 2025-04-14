from typing import List, Dict

from bson import ObjectId
from pymongo import MongoClient

from src.data.models.appointment import Appointment
from src.data.repositories.appointmentrepo.appointments import Appointments
from src.data.repositories.doctorrepositories.doctorrepository import DoctorRepository
from src.data.repositories.patientrepositories.patients import Patients


class AppointmentRepository(Appointments):

    def __init__(self, patient_repo: Patients, doctor_repo: DoctorRepository):
        self.patient_repo = patient_repo
        self.doctor_repo = doctor_repo
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['medical_report_management_system']
        self.collection = self.database['appointments']

    def create_appointment(self, appointment: Appointment):
        appointment_data = {
            'patient_id': appointment.patient_id.id,
            'doctor_id': appointment.doctor_id.id,
            'date_time': appointment.date_time,
            'reason': appointment.reason,
            'status': appointment.status
        }
        return str(self.collection.insert_one(appointment_data).inserted_id)

    def get_all_appointment(self) -> List[Dict]:
        return list(self.collection.find())

    def find_by_id(self, user_id):
        appointment_data = self.collection.find_one({"_id": ObjectId(user_id)})
        if appointment_data:
            patient = self.patient_repo.find_by_id(appointment_data['patient_id'])
            doctor = self.doctor_repo.find_by_id(appointment_data['doctor_id'])
            return Appointment(
                patient_id=patient['patient_id'],
                doctor_id=doctor['doctor_id'],
                date_time=appointment_data["date_time"],
                reason=appointment_data["reason"],
                # id=str(appointment_data["_id"])
            )
        return None