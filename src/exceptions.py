class ServerAPIError(Exception):
    pass


class NotFoundError(ServerAPIError):
    pass


class ConflictError(ServerAPIError):
    pass


class UserAlreadyExistsError(ConflictError):
    pass


class UserNotFoundError(NotFoundError):
    pass
