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

            profile_data = {
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'date_of_birth': data.get('date_of_birth'),
                'phone_number': data.get('phone_number'),
                'gender': data.get('gender'),
                'medical_history': data.get('medical_history')
            }

            required = ['first_name', 'last_name', 'date_of_birth']
            if not all(profile_data.get(field) for field in required):
                return jsonify({"error": f"Missing required fields: {required}"}), 400

            profile_id = self.patient_service.create_patient_profile(data['user_id'], profile_data)
            return jsonify({"message": "Profile created", "id": profile_id}), 201
        except JsonifyError:
            return jsonify({"error"}), 400
