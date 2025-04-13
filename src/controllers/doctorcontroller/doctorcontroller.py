from flask import request, jsonify

from src.exceptions.exceptions import *
from src.services.doctorservices.doctorservice import DoctorService


class DoctorController:

    def __init__(self, doctor_service: DoctorService):
        self.doctor_service = doctor_service

    def create_doctor_profile(self):
        try:
            data = request.get_json()
            if 'doctor_id' not in data:
                return jsonify({"error": "User ID required"}), 400

            profile_data = {
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'phone_number': data.get('phone_number'),
                'gender': data.get('gender'),
                'specialization': data.get('specialization'),
                # 'is_available': data.get('is_available')
            }

            # required = ['first_name', 'last_name', 'date_of_birth']
            # if not all(profile_data.get(field) for field in required):
            #     return jsonify({"error": f"Missing required fields: {required}"}), 400

            profile_id = self.doctor_service.create_doctor_profile(data['doctor_id'], profile_data)
            return jsonify({"message": "Profile created",
                            "id": profile_id}), 201
        except JsonifyError:
            return jsonify({"error"}), 400
