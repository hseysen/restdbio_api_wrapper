import requests
from .Exceptions import *


class Decorators:
    @staticmethod
    def url_to_get(method):
        def get_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            response = requests.get(url, headers=obj.header)
            response_code_handler(response.status_code)
            return response.json()
        return get_request_performer
    
    @staticmethod
    def url_to_post(method):
        def post_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            post_data = args[-1]
            response = requests.post(url, post_data, headers=obj.header)
            response_code_handler(response.status_code)
        return post_request_performer

    @staticmethod
    def url_to_put(method):
        def put_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            put_data = args[-1]
            response = requests.put(url, put_data, headers=obj.header)
            response_code_handler(response.status_code)
        return put_request_performer

    @staticmethod
    def url_to_patch(method):
        def patch_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            patch_data = args[-1]
            response = requests.patch(url, patch_data, headers=obj.header)
            response_code_handler(response.status_code)
        return patch_request_performer
    
    @staticmethod
    def url_to_delete(method):
        def delete_request_performer(obj, *args, **kwargs):
            url = method(obj, *args, **kwargs)
            response = requests.delete(url, headers=obj.header)
            response_code_handler(response.status_code)
        return delete_request_performer