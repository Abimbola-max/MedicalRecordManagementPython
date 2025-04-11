from flask import Flask

from src.controllers.patientcontroller.patientcontroller import PatientController
from src.controllers.usercontroller import UserController
from src.data.repositories.patientrepo.patients import Patients
from src.data.repositories.users import Users
from src.services.patientservice.patientservice import PatientService
from src.services.usersauthentication.userservices import UserServices

app = Flask(__name__)
user_repo = Users()
user_service = UserServices(user_repo)
user_controller = UserController(user_service)

patient_repo = Patients(user_repo)
patient_service = PatientService(patient_repo, user_repo)
patient_controller = PatientController(patient_service)


@app.route('/register', methods=['POST'])
def register_user():
    return user_controller.register()

@app.route('/login', methods=['POST'])
def login():
    return user_controller.login()

@app.route('/profiles', methods=['POST'])
def create_profile():
    return patient_controller.create_patient_profile()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
