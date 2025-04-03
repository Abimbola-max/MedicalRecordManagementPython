class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ProfileDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)