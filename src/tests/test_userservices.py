from unittest import TestCase

from src.data.models.passwordencrypt import PasswordEncrypt
from src.data.models.role import Role
from src.data.repositories.users import Users
from src.exceptions.exceptions import InvalidEmailPatternException, NullException, InvalidNameLengthException
from src.services.usersauthentication.userservices import UserServices


class TestUserServices(TestCase):

    def setUp(self):
        self.user_repo = Users()
        self.user_service = UserServices(self.user_repo)

    def tearDown(self):
        self.user_repo.collection.delete_many({})
        self.user_repo.close_client()

    def test_that_user_can_be_registered(self):
        username = "abisoyeabimbola"
        email = "abisoye4@gmail.com"
        password = "password"
        role = Role.PATIENT

        user_id = self.user_service.register_user(username, email, password, role)
        self.assertIsNotNone(user_id)

        saved_user = self.user_repo.find_user_by(email)
        self.assertTrue(saved_user)
        self.assertEqual(saved_user.roles, ["PATIENT"])

    def test_that_a_user_can_be_registered_with_multiple_roles(self):
        username = "abisoyeaishat"
        email = "abisoye231@gmail.com"
        password = "passwordfr"
        roles = [Role.DOCTOR, Role.PATIENT]

        user_id = self.user_service.register_user(username, email, password, roles)
        self.assertIsNotNone(user_id)

        saved_user = self.user_repo.find_user_by(email)
        self.assertTrue(saved_user)
        self.assertIn("DOCTOR", saved_user.roles)
        self.assertIn("PATIENT", saved_user.roles)
        self.assertEqual(len(saved_user.roles), 2)

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
        email = "abisoye2021@gmail.com"
        password = "password"
        role = Role.PATIENT
        # user = User(username, email, password, role)
        user_id = self.user_service.register_user(username, email, password, role)
        self.assertIsNotNone(user_id)
        self.assertTrue(self.user_repo.find_user_by("abisoye2021@gmail.com"))
        login_email = "abisoye2021@gmail.com"
        login_password = "password"
        hashed = PasswordEncrypt.encrypt_password(password)
        self.assertTrue(PasswordEncrypt.verify_password(password, hashed))

        self.assertIsNotNone(self.user_service.login(login_email, login_password))
        # self.assertEqual(email, login_email)
        #
        # print("test own " + PasswordEncrypt.verify_password(password, user_id.password))
