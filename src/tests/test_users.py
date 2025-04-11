from unittest import TestCase

from src.data.models.role import Role
from src.data.models.user import User
from src.data.repositories.users import Users


class TestUsers(TestCase):

    def setUp(self):
        self.users = Users()
        # self.users.collection.delete_many({})

    def tearDown(self):
        # self.users.collection.delete_many({})
        self.users.cleanup_invalid_passwords()
        self.users.close_client()

    def test_that_users_can_be_saved(self):
        self.assertEqual(self.users.count_users(), 0)
        first_user = User("favour-rite", "abisoye@gmail.com", "password", ["PATIENT"])
        self.users.save_user(first_user)
        self.assertEqual(self.users.count_users(), 1)
        second_user = User("hamid", "hamid@gmail.com", "password", ["DOCTOR"])
        self.users.save_user(second_user)
        self.assertEqual(self.users.count_users(), 2)

