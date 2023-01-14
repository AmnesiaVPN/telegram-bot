class ApplicationError(Exception):
    pass


class ServerAPIError(ApplicationError):
    status_code = 500


class NotFoundError(ServerAPIError):
    status_code = 404


class ConflictError(ServerAPIError):
    status_code = 409


class GoneError(ServerAPIError):
    status_code = 410


class UserAlreadyExistsError(ConflictError):
    pass


class UserNotFoundError(NotFoundError):
    pass


class UserAlreadyActivatedPromocodeError(ConflictError):
    pass


class PromocodeNotFoundError(NotFoundError):
    pass


class PromocodeWasActivatedError(ConflictError):
    pass


class PromocodeWasExpiredError(GoneError):
    pass
