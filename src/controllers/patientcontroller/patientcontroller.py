from flask import request, jsonify

from src.exceptions.exceptions import JsonifyError
from src.services.patientservice.patientservice import PatientService


class PatientController:

    def __init__(self, patient_service: PatientService):
        self.patient_service = patient_service

    def create_patient_profile(self):
        try:
            data = request.get_json()
            if 'user_id' not in data:
                return jsonify({"error": "User ID required"}), 400

            profile_id = self.patient_service.create_patient_profile(data['user_id'], data)
            return jsonify({"message": "Profile created", "id": profile_id}), 201
        except JsonifyError:
            return jsonify({"error"}), 400
