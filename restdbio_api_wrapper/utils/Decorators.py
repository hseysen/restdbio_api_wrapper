import requests
from .Exceptions import *


class Decorators:
    """
    All decorators used within the package are defined here.
    """
    @staticmethod
    def url_to_get(method):
        """
        Decorates a method that returns a url, converting it into a get_request_performer.

        Parameters:
        method                  --- the method to be decorated.

        Returns:
        get_request_performer   --- the modified function that performs the get request.
        """
        def get_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            response = requests.get(url, headers=obj.header)
            response_code_handler(response.status_code)
            return response.json()
        get_request_performer.__name__ = method.__name__
        get_request_performer.__doc__ = method.__doc__
        return get_request_performer
    
    @staticmethod
    def url_to_post(method):
        """
        Decorates a method that returns a url, converting it into a post_request_performer.

        Parameters:
        method                   --- the method to be decorated.

        Returns:
        post_request_performer   --- the modified function that performs the post request.
        """
        def post_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            post_data = args[-1]
            response = requests.post(url, post_data, headers=obj.header)
            response_code_handler(response.status_code)
        post_request_performer.__name__ = method.__name__
        post_request_performer.__doc__ = method.__doc__
        return post_request_performer

    @staticmethod
    def url_to_put(method):
        """
        Decorates a method that returns a url, converting it into a put_request_performer.

        Parameters:
        method                  --- the method to be decorated.

        Returns:
        put_request_performer   --- the modified function that performs the put request.
        """
        def put_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            put_data = args[-1]
            response = requests.put(url, put_data, headers=obj.header)
            response_code_handler(response.status_code)
        put_request_performer.__name__ = method.__name__
        put_request_performer.__doc__ = method.__doc__
        return put_request_performer

    @staticmethod
    def url_to_patch(method):
        """
        Decorates a method that returns a url, converting it into a patch_request_performer.

        Parameters:
        method                    --- the method to be decorated.

        Returns:
        patch_request_performer   --- the modified function that performs the patch request.
        """
        def patch_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            patch_data = args[-1]
            response = requests.patch(url, patch_data, headers=obj.header)
            response_code_handler(response.status_code)
        patch_request_performer.__name__ = method.__name__
        patch_request_performer.__doc__ = method.__doc__
        return patch_request_performer
    
    @staticmethod
    def url_to_delete(method):
        """
        Decorates a method that returns a url, converting it into a delete_request_performer.

        Parameters:
        method                     --- the method to be decorated.

        Returns:
        delete_request_performer   --- the modified function that performs the delete request.
        """
        def delete_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            response = requests.delete(url, headers=obj.header)
            response_code_handler(response.status_code)
        delete_request_performer.__name__ = method.__name__
        delete_request_performer.__doc__ = method.__doc__
        return delete_request_performer