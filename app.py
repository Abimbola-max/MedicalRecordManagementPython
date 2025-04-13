from flask import Flask

from src.controllers.doctorcontroller.doctorcontroller import DoctorController
from src.controllers.patientcontroller.patientcontroller import PatientController
from src.controllers.usercontrollers.usercontroller import UserController
from src.data.repositories.doctorrepositories.doctorrepository import DoctorRepository
from src.data.repositories.patientrepositories.patients import PatientRepo, Patients
from src.data.repositories.userrepositories.users import Users
from src.services.doctorservices.doctorservice import DoctorService
from src.services.patientservice.patientservice import PatientService
from src.services.usersauthentication.userservices import UserServices

app = Flask(__name__)
user_repo = Users()
user_service = UserServices(user_repo)
user_controller = UserController(user_service)

patient_repo = Patients(user_repo)
patient_service = PatientService(patient_repo, user_repo)
patient_controller = PatientController(patient_service)

doctor_repo = DoctorRepository(user_repo)
doctor_service = DoctorService(doctor_repo, user_repo)
doctor_controller = DoctorController(doctor_service)


@app.route('/register', methods=['POST'])
def register_user():
    return user_controller.register()

@app.route('/login', methods=['POST'])
def login():
    return user_controller.login()

@app.route('/patient_profiles', methods=['POST'])
def create_profile():
    return patient_controller.create_patient_profile()

@app.route('/doctor_profile', methods=['POST'])
def create_dr_profile():
    return doctor_controller.create_doctor_profile()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
