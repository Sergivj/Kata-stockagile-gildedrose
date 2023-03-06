class CustomExceptions(Exception):
    def __init__(self, message=''):
        super().__init__(message)
        self.message = message


class InvalidQualityException(CustomExceptions):
    pass
