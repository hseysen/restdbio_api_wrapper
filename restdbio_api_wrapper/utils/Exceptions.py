"""
All exceptions within the module are defined and handled here.
"""

class ExceptionsMeta(type):
    """
    Metaclass for the exceptions I will be declaring. Since all exceptions are structurally the same, I decided using a metaclass would prove useful.
    """
    def __new__(cls, name, bases=tuple(), dct=dict()):
        x = super().__new__(cls, name, bases, dct)
        
        def __init__(self, message):
            Exception.__init__(self, message)
        
        x.__init__ = __init__
        return x


def response_code_handler(response_code):
    """
    Maps the response code to the corresponding exception to be thrown. For some exceptions, I tried to make the message
    a bit more straightforward, with the possible reason why the exception may have occurred. For others, I used the generalized messages.

    Parameters:
    response_code   --- the status code received from the HTTP request. Usually a Response object's status_code attribute.
    """
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
    """
    Intended to be thrown when HTTP response code is 400.
    """
    pass


class Unauthorized(Exception, metaclass=ExceptionsMeta):
    """
    Intended to be thrown when HTTP response code is 401.
    """
    pass


class Forbidden(Exception, metaclass=ExceptionsMeta):
    """
    Intended to be thrown when HTTP response code is 403.
    """
    pass


class NotFound(Exception, metaclass=ExceptionsMeta):
    """
    Intended to be thrown when HTTP response code is 404.
    """
    pass


class RequestTimeout(Exception, metaclass=ExceptionsMeta):
    """
    Intended to be thrown when HTTP response code is 408.
    """
    pass


class Conflict(Exception, metaclass=ExceptionsMeta):
    """
    Intended to be thrown when HTTP response code is 409.
    """
    pass


class InternalServerError(Exception, metaclass=ExceptionsMeta):
    """
    Intended to be thrown when HTTP response code is 410.
    """
    pass