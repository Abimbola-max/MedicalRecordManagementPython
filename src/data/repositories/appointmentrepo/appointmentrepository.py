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

    def save(self, appointment: Appointment):
        appointment_data = {
            'patient_id': appointment.patient_id.id,
            'doctor_id': appointment.doctor_id.id,
            'date_time': appointment.date_time,
            'reason': appointment.reason,
            'status': appointment.status
        }
        if appointment.appointment_id:
            self.collection.update_one(
                {"_id": ObjectId(appointment.appointment_id)},
                {"$set": appointment_data}
            )
            return appointment.appointment_id
        else:
            result = self.collection.insert_one(appointment_data)
            return str(result.inserted_id)
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
                appointment_id=str(appointment_data["appointment_id"])
            )
        return None

    def find_by_doctor_id(self, doctor_id):
        appointments = []

        doctor = self.doctor_repo.find_by_id(doctor_id)
        if not doctor:
            return []

        cursor = self.collection.find({"doctor_id": doctor_id})  # corrected line
        for appointment_data in cursor:
            try:
                patient = self.patient_repo.find_by_id(appointment_data['patient_id'])
                doctor = self.doctor_repo.find_by_id(appointment_data['doctor_id'])
            except Exception as e:
                print(f"Error fetching patient or doctor for appointment {appointment_data.get('_id')}: {e}")
                continue

            if patient and doctor:
                appointment = Appointment(
                    patient_id=patient,
                    doctor_id=doctor,
                    date_time=appointment_data.get("date_time"),
                    appointment_id=str(appointment_data.get('appointment_id'))
                )
                appointments.append(appointment)

        return appointments



