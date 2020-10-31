from ..utils import Decorators


class CollectionAPI:
    """
    The API calls defined here are used to make calls to your collection in your database.
    """
    TEMPLATE_URL_COLLECTION = "https://{}.restdb.io/rest/{}"
    TEMPLATE_URL_COLLECTION_ID = "https://{}.restdb.io/rest/{}/{}"
    TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION = "https://{}.restdb.io/rest/{}/{}/{}"
    TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION_ID = "https://{}.restdb.io/rest/{}/{}/{}/{}"
    
    def __init__(self, dburl, x_apikey):
        """
        Parameters:
        dburl      --- represents the beginning of the url to your database. Usually the same as your database name on your dashboard.
        x_apikey   --- represents the API key you will be using to access your database. Go to your Database Settings and choose API to see your API key.
        """
        self.dburl = dburl
        self.x_apikey = x_apikey
        self.header = {"x-apikey": self.x_apikey}

    @Decorators.url_to_get
    def get_records_from_collection(self, collection_name, q={}, _filter=None, _sort=None, _dir=None, skip=None, _max=None, groupby=None, aggregate=None):
        """
        Performs a get request to the collection at the database. The queries can be specialized with the keyword arguments.

        Parameters:
        collection_name   --- name of the collection to retrieve information from.

        Keyword Arguments: (visit https://restdb.io/media/restdb-cheat-sheet.pdf for more info)
        q                 --- specifies the search query.
        _filter           --- filters the search results.
        _sort             --- sorts the results according to a column value.
        _dir              --- the direction of the sort. -1 for reverse. 1 by default.
        skip              --- how many results to be skipped from the beginning.
        _max              --- how many results to be returned at maximum.
        groupby           --- grouping certain results according to the given column value.
        aggregate         --- usually used with groupby. performs aggregation functions (sum, avg, min, max, count) on given columns of the result.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION.format(self.dburl, collection_name)

        url += "?q=" + str(q)

        if _filter is not None:
            url += "&filter=" + _filter
        
        if _sort is not None:
            if type(_sort) is str:
                url += "&sort=" + _sort
            else:
                for sort_parameter in _sort:
                    url += "&sort=" + sort_parameter
        
        if _dir is not None:
            url += "&dir=" + str(_dir)
        
        if skip is not None:
            url += "&skip=" + str(skip)
        
        if _max is not None:
            url += "&max=" + str(_max)
        
        if groupby is not None:
            url += "&groupby=" + groupby
        
        if aggregate is not None:
            for aggregator in aggregate:
                url += "&aggregate=" + aggregator.upper() + ":" + aggregate[aggregator]
        
        url = url.replace("'", '"')
        return url
    
    @Decorators.url_to_get
    def get_record_from_collection(self, collection_name, record_id):
        """
        Performs a get request to the collection at the database with the specified ID.

        Parameters:
        collection_name   --- name of the collection to retrieve information from.
        record_id         --- ID of the record to be fetched.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url
    
    @Decorators.url_to_get
    def get_records_from_subcollection(self, collection_name, record_id, subcollection_name):
        """
        Performs a get request to the subcollection under the record of the collection with the specified ID at the database.

        Parameters:
        collection_name      --- name of the collection to retrieve information from.
        record_id            --- ID of the record.
        subcollection_name   --- name of the subcollection to retrieve information from.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION.format(self.dburl, collection_name, record_id, subcollection_name)
        return url
    
    @Decorators.url_to_get
    def get_record_from_subcollection(self, collection_name, record_id, subcollection_name, record_id2):
        """
        Performs a get request to the specified record in the subcollection under the record of the collection with the specified ID at the database.

        Parameters:
        collection_name      --- name of the collection to retrieve information from.
        record_id            --- ID of the record.
        subcollection_name   --- name of the subcollection to retrieve information from.
        record_id2           --- ID of the record within the subcollection to be fetched.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION_ID.format(self.dburl, collection_name, record_id, subcollection_name, record_id2)
        return url
    
    @Decorators.url_to_post
    def post_new_record_on_collection(self, collection_name, new_record, validate=True):
        """
        Performs a post request to the collection at the database.

        Parameters:
        collection_name   --- name of the collection to send information.
        new_record        --- the new data to be sent to the database.

        Keyword Arguments:
        validate          --- whether or not validation should be performed. set to False for slightly faster performance (not recommended at early stages).
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION.format(self.dburl, collection_name)
        if not validate:
            url += "?validate=false"
        return url

    @Decorators.url_to_post
    def post_new_record_on_subcollection(self, collection_name, record_id, subcollection_name, new_record, validate=True):
        """
        Performs a post request to the collection at the database.

        Parameters:
        collection_name      --- name of the collection to send information.
        record_id            --- the ID of the record.
        subcollection_name   --- name of the subcollection to send information.
        new_record           --- the new data to be sent to the database.

        Keyword Arguments:
        validate          --- whether or not validation should be performed. set to False for slightly faster performance (not recommended at early stages).
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION.format(self.dburl, collection_name, record_id, subcollection_name)
        if not validate:
            url += "?validate=false"
        return url

    @Decorators.url_to_put
    def put_existing_record_in_collection(self, collection_name, record_id, new_record):
        """
        Performs a put request to the collection at the database with the specified ID.

        Parameters:
        collection_name   --- name of the collection to send information.
        record_id         --- ID of the record to be modified.
        new_record        --- the new record to be sent.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url

    @Decorators.url_to_patch
    def patch_existing_record_in_collection(self, collection_name, record_id, new_record):
        """
        Performs a patch request to the collection at the database with the specified ID.

        Parameters:
        collection_name   --- name of the collection to send information.
        record_id         --- ID of the record to be updated.
        new_record        --- the new record to be sent.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url
    
    @Decorators.url_to_delete
    def delete_record_by_id(self, collection_name, record_id):
        """
        Performs a delete request to the collection at the database with the specified ID.

        Parameters:
        collection_name   --- name of the collection to delete record from.
        record_id         --- ID of the record to be deleted.
        """
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url
    
    @Decorators.url_to_delete
    def delete_record_by_query(self, collection_name, q={}):
        """
        Performs a delete request to the collection at the database. Specialized with a query.

        Parameters:
        collection_name   --- name of the collection to delete record from.
        q                 --- query dictionary for deletion. cannot be empty.
        """
        if not q:
            raise ValueError("q cannot be empty")
        url = CollectionAPI.TEMPLATE_URL_COLLECTION.format(self.dburl, collection_name)
        url += "/*?q=" + str(q)
        url = url.replace("'", '"')
        return url