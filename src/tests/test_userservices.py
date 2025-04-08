from unittest import TestCase

from src.data.models.role import Role
from src.data.repositories.users import Users
from src.exceptions.exceptions import InvalidEmailPatternException, NullException, InvalidNameLengthException
from src.services.authentication.userservices import UserServices


class TestUserServices(TestCase):

    def setUp(self):
        self.user_repo = Users()
        self.user_service = UserServices(self.user_repo)

    def tearDown(self):
        self.user_repo.close_client()

    def test_that_user_can_be_registered(self):
        username = "abisoyeabimbola"
        email = "abisoye@gmail.com"
        password = "password"
        role = Role.PATIENT
        # user = User(username, email, password, role)
        user_id = self.user_service.register_user(username, email, password, role)
        self.assertIsNotNone(user_id)
        self.assertTrue(self.user_repo.find_user_by("abisoye@gmail.com"))

    def test_register_user_invalid_email(self):
        with self.assertRaises(InvalidEmailPatternException):
            username = "abisoyeabimbola"
            email = "abis.oye.gmail.com"
            password = "password"
            role = Role.PATIENT
            user_id = self.user_service.register_user(username, email, password, role)
            self.assertFalse(self.user_repo.find_user_by("abis.oye.gmail.com"))

    def test_that_user_cannot_register_with_empty_username_field(self):
        with self.assertRaises((NullException, InvalidNameLengthException)):
            username = " "
            email = "abisoye@gmail.com"
            password = "password"
            role = Role.PATIENT
            user_id = self.user_service.register_user(username, email, password, role)
            self.assertFalse(self.user_repo.find_user_by("abisoye@gmail.com"))

    def test_that_user_can_register_and_login_with_valid_details(self):
        username = "abisoyeabimbola"
        email = "abisoye@gmail.com"
        password = "password"
        role = Role.PATIENT
        # user = User(username, email, password, role)
        user_id = self.user_service.register_user(username, email, password, role)
        self.assertIsNotNone(user_id)
        self.assertTrue(self.user_repo.find_user_by("abisoye@gmail.com"))
        user_login = self.user_service.login(email, password)
