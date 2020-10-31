from .apis import *


class Connection:
    """
    The objects of this class represent a connection between the database and the program.
    Initialized using the database url (<dburl>) and the x-apikey.
    Automatically initializes a CollectionAPI object as its attribute. For more on CollectionAPI, use help(Connection(dburl, x_apikey).collection_api)
    """
    def __init__(self, dburl, x_apikey):
        """
        Parameters:
        dburl      --- represents the beginning of the url to your database. Usually the same as your database name on your dashboard.
        x_apikey   --- represents the API key you will be using to access your database. Go to your Database Settings and choose API to see your API key.
        """
        self.dburl = dburl
        self.x_apikey = x_apikey
        self.collection_api = CollectionAPI(self.dburl, self.x_apikey)