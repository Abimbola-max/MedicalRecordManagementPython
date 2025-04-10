from pymongo import MongoClient

from src.data.models.user import User


class MedicalRepository:

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['medical_report_management_system']
        self.users = self.db.users
        self.patients = self.db.patients
        self.doctors = self.db.doctors
        self.appointments = self.db.appointments


    def save_user_a(self, user: User):
        user_data = {
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'roles': [role.value for role in user.roles]
        }
        return user_data

    def save_patient_profile(self, patient: PatientProfile) -> str:
        patient_data = {
            'user_id': str(patient.id),
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'date_of_birth': patient.date_of_birth,
            'phone_number': patient.phone_number,
            'gender': patient.gender.value,
            'medical_history': patient.medical_history
        }
        return str(self.patients.insert_one(patient_data).inserted_id)

    def find_patient_profile(self, user_id: str) -> Optional[PatientProfile]:
        data = self.patients.find_one({'user_id': user_id})
        if data:
            user_data = self.users.find_one({'_id': user_id})
            return PatientProfile(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                date_of_birth=data['date_of_birth'],
                phone_number=data['phone_number'],
                gender=Gender(data['gender']),
                medical_history=data['medical_history']
            )
        return None

    def get_available_doctors(self) -> List[Doctor]:
        return [self._doc_to_doctor(d) for d in self.doctors.find({'is_available': True})]

    def update_doctor_availability(self, doctor_email: str, available: bool):
        self.doctors.update_one(
            {'email': doctor_email},
            {'$set': {'is_available': available}}
        )

    def create_appointment(self, appointment: Appointment) -> str:
        appointment_data = {
            'patient_id': str(appointment.patient.id),
            'doctor_id': str(appointment.doctor.id),
            'date_time': appointment.date_time,
            'reason': appointment.reason,
            'status': appointment.status
        }
        return str(self.appointments.insert_one(appointment_data).inserted_id)

    def get_all_appointments(self) -> List[Dict]:
        return list(self.appointments.find())

    def _doc_to_doctor(self, doc) -> Doctor:
        return Doctor(
            username=doc['username'],
            email=doc['email'],
            password=doc['password'],
            first_name=doc['first_name'],
            last_name=doc['last_name'],
            phone_number=doc['phone_number'],
            specialization=Specialization(doc['specialization'])
        )