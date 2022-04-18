from lib2to3.pgen2.token import BACKQUOTE


class BaseError(Exception):
    pass


class RunValidationError(BaseError):
    pass  # TODO


class ValidationError(BaseError):
    pass