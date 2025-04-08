from unittest import TestCase
from unittest.mock import Mock

from src.data.models.passwordencrypt import PasswordEncrypt
from src.data.models.patientprofile import PatientProfile
from src.data.models.user import User
from src.data.repositories.userrepository import UserRepository
from src.exceptions.exceptions import NotFoundException
from src.services.authentication.userservices import UserServices


class TestUserServices(TestCase):

    # def setUp(self):
    #     self.user_repo_mock = Mock(spec=UserRepository)
    #     self.password_encrypt_mock = Mock(spec=PasswordEncrypt)
    #     self.user_service = UserServices(self.user_repo_mock)
    #     self.user_service.password_encrypt = self.password_encrypt_mock
        # self.user_repository = UserRepository()
        # self.user_service = UserServices(self.user_repository)

        # self.user_data = User (
        #     username = "testuser",
        #     email = "test@example.com",
        #     password = "password123",
        #     role = "patient",
            # user_id = "123",
            # first_name = "Test",
            # last_name = "User",
            # date_of_birth = "1990-01-01",
            # phone_number = "1234567890",
            # medical_history = ["eggs", "never had surgeies"]
        # )

    # def test_register_success(self):
    #     new_user = User(email="test@example.com", password="password", username="testuser", role="patient")
    #     self.user_repo_mock.find_user_by.return_value = None
    #     self.password_encrypt_mock.encrypt_password.return_value = "hashed_password"
    #     result = self.user_service.register(new_user)
    #     self.assertTrue(result)
    #     self.user_repo_mock.find_user_by.assert_called_once_with("test@example.com")
    #     self.password_encrypt_mock.encrypt_password.assert_called_once_with("password")
    #     self.user_repo_mock.save_user.assert_called_once()
    #     saved_user = self.user_repo_mock.save_user.call_args
    #     self.assertEqual(saved_user.password, "hashed_password")


    # def test_that_user_can_register(self):
    #     pass
    #
    #
    #
    #     def test_register_fail_email_exists(self):
    #         existing_user = {"email": "test@example.com"}
    #         new_user = User(email="test@example.com", password="password", username="testuser", role="patient",
    #                         first_name="Test", last_name="User", date_of_birth="2000-01-01",
    #                         phone_number="123-456-7890", medical_history="")
    #         self.user_repo_mock.find_user_by.return_value = existing_user
    #         result = self.user_service.register(new_user)
    #         self.assertFalse(result)
    #         self.user_repo_mock.find_user_by.assert_called_once_with("test@example.com")
    #         self.password_encrypt_mock.encrypt_password.assert_not_called()
    #         self.user_repo_mock.save_user.assert_not_called()
    #
    #     def test_login_success_patient(self):
    #         user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'hashed_password',
    #                      'user_id': 1, 'first_name': 'Test', 'last_name': 'User', 'date_of_birth': '2000-01-01',
    #                      'phone_number': '123-456-7890', 'medical_history': '', 'role': 'patient'}
    #         self.user_repo_mock.find_user_by.return_value = user_data
    #         self.password_encrypt_mock.verify_password.return_value = True
    #         profile = self.user_service.login('test@example.com', 'password')
    #         self.assertIsInstance(profile, PatientProfile)
    #         self.assertEqual(profile.username, 'testuser')
    #         self.user_repo_mock.find_user_by.assert_called_once_with('test@example.com')
    #         self.password_encrypt_mock.verify_password.assert_called_once_with('password', 'hashed_password')
    #
    #     def test_login_fail_user_not_found(self):
    #         self.user_repo_mock.find_user_by.return_value = None
    #         with self.assertRaises(NotFoundException):
    #             self.user_service.login('nonexistent@example.com', 'password')
    #         self.user_repo_mock.find_user_by.assert_called_once_with('nonexistent@example.com')
    #         self.password_encrypt_mock.verify_password.assert_not_called()
    #
    #     def test_login_fail_incorrect_password(self):
    #         user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'hashed_password',
    #                      'user_id': 1, 'first_name': 'Test', 'last_name': 'User', 'date_of_birth': '2000-01-01',
    #                      'phone_number': '123-456-7890', 'medical_history': '', 'role': 'patient'}
    #         self.user_repo_mock.find_user_by.return_value = user_data
    #         self.password_encrypt_mock.verify_password.return_value = False
    #         with self.assertRaises(NotFoundException):
    #             self.user_service.login('test@example.com', 'wrong_password')
    #         self.user_repo_mock.find_user_by.assert_called_once_with('test@example.com')
    #         self.password_encrypt_mock.verify_password.assert_called_once_with('wrong_password', 'hashed_password')
    #
    #     def test_create_user_profile_patient(self):
    #         user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'hashed_password',
    #                      'user_id': 1, 'first_name': 'Test', 'last_name': 'User', 'date_of_birth': '2000-01-01',
    #                      'phone_number': '123-456-7890', 'medical_history': '', 'role': 'patient'}
    #         profile = self.user_service._UserService__create_user_profile(user_data)  # Accessing static method
    #         self.assertIsInstance(profile, PatientProfile)
    #         self.assertEqual(profile.username, 'testuser')
    #
    # if __name__ == '__main__':
    #     unittest.main()


