import re

from src.exceptions.exceptions import *


class Validator:

   @staticmethod
   def validate_first_name(first_name) -> bool:
       if not first_name:
           raise NullException("First Name field is required")
       if not first_name.strip():
           raise InvalidNameLengthException("No spaces allowed amongst the letters.")
       if len(first_name) < 3 or not first_name.isalpha():
           raise InvalidNameLengthException("First Name must be at least 3 characters long and contain only letters.")
       return True

   @staticmethod
   def validate_last_name(last_name: str) -> bool:
       if not last_name:
           raise NullException("Last Name field is required")
       if not last_name.strip():
           raise InvalidNameLengthException("No spaces allowed amongst the letters.")
       if len(last_name) < 3:
           raise InvalidNameLengthException("Last Name must be at least 3 characters long and contain only letters.")
       return True

   @staticmethod
   def validate_email(email_input: str) -> bool:
       if not email_input:
           raise NullException("Email field is required")

       if not isinstance(email_input, str):
           raise InvalidEmailPatternException("Email must be a string")

       if not email_input.strip():
           raise InvalidEmailPatternException("Email should not be only spaces")

       email_pattern = r'^[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.(com|africa|org|ng|yahoo)$'

       if email_input.endswith(".") or email_input.startswith("."):
           raise InvalidEmailPatternException("Email should not end with a period")

       if not re.match(email_pattern, email_input):
           raise InvalidEmailPatternException("Invalid email address.")


       return True


   @staticmethod
   def validate_password(password: str) -> bool:
       if not password:
           raise NullException("Password field is required")
       if not password.strip():
           raise InvalidPasswordLengthException("Invalid.")
       if len(password) < 5:
           raise InvalidPasswordLengthException("Password must be at least 5 characters long and contain only letters.")
       return True