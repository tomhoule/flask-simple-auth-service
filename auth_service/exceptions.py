class UnauthenticatedException(Exception):
    message = None

    def __init__(self, message="Not authenticated"):
        self.message = message
        super().__init__()


class UnauthorizedException(Exception):
    message = None

    def __init__(self, message="Not authorized"):
        self.message = message
        super().__init__()
