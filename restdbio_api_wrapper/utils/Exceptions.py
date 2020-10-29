class ExceptionsMeta(type):
    def __new__(cls, name, bases=tuple(), dct=dict()):
        x = super().__new__(cls, name, bases, dct)
        
        def __init__(self, message):
            Exception.__init__(self, message)
        
        x.__init__ = __init__
        return x


def response_code_handler(response_code):
    if response_code == 400:
        raise BadRequest("May be because your request data format mismatched the format on database, or the record primary key already existed.")
    if response_code == 401:
        raise Unauthorized("Check your dburl and x-apikey.")
    if response_code == 403:
        raise Forbidden("The request was a legal request, but the server is refusing to respond to it.")
    if response_code == 404:
        raise NotFound("The server has not found anything matching your request data.")
    if response_code == 408:
        raise RequestTimeout("The server did not respond within the specified time.")
    if response_code == 409:
        raise Conflict("The request could not be completed due to a conflict with the current state of the resource.")
    if response_code == 500:
        raise InternalServerError("The server encountered an unexpected condition which prevented it from fulfilling the request.")


class BadRequest(Exception, metaclass=ExceptionsMeta):
    pass


class Unauthorized(Exception, metaclass=ExceptionsMeta):
    pass


class Forbidden(Exception, metaclass=ExceptionsMeta):
    pass


class NotFound(Exception, metaclass=ExceptionsMeta):
    pass


class RequestTimeout(Exception, metaclass=ExceptionsMeta):
    pass


class Conflict(Exception, metaclass=ExceptionsMeta):
    pass


class InternalServerError(Exception, metaclass=ExceptionsMeta):
    pass