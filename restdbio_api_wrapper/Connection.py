from .apis.CollectionAPI import *


class Connection:
    def __init__(self, dburl, x_apikey):
        self.dburl = dburl
        self.x_apikey = x_apikey
        self.collection_api = CollectionAPI(self.dburl, self.x_apikey)