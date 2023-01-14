class ApplicationError(Exception):
    pass


class ServerAPIError(ApplicationError):
    pass


class NotFoundError(ServerAPIError):
    pass


class ConflictError(ServerAPIError):
    pass


class UserAlreadyExistsError(ConflictError):
    pass


class UserNotFoundError(NotFoundError):
    pass


class UserAlreadyActivatedPromocodeError(ConflictError):
    pass


class PromocodeNotFoundError(NotFoundError):
    pass
