from unittest import TestCase

from src.data.models.passwordencrypt import PasswordEncrypt


class TestPasswordEncrypt(TestCase):


    password = "password"
    hashed_password = PasswordEncrypt.encrypt_password(password)
    print(f"Generated Hash: {hashed_password}")

    is_valid = PasswordEncrypt.verify_password(password, hashed_password)
    print(f"Verification Result: {is_valid}")

