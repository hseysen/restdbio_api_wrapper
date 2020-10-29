from restdbio_api_wrapper.utils.Decorators import Decorators


class CollectionAPI:
    TEMPLATE_URL_COLLECTION = "https://{}.restdb.io/rest/{}"
    TEMPLATE_URL_COLLECTION_ID = "https://{}.restdb.io/rest/{}/{}"
    TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION = "https://{}.restdb.io/rest/{}/{}/{}"
    TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION_ID = "https://{}.restdb.io/rest/{}/{}/{}/{}"
    
    def __init__(self, dburl, x_apikey):
        self.dburl = dburl
        self.x_apikey = x_apikey
        self.header = {"x-apikey": self.x_apikey}

    @Decorators.url_to_get
    def get_records_from_collection(self, collection_name, q={}, _filter=None, _sort=None, _dir=None, skip=None, _max=None, groupby=None, aggregate=None):
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
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url
    
    @Decorators.url_to_get
    def get_records_from_subcollection(self, collection_name, record_id, subcollection_name):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION.format(self.dburl, collection_name, record_id, subcollection_name)
        return url
    
    @Decorators.url_to_get
    def get_record_from_subcollection(self, collection_name, record_id, subcollection_name, record_id2):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION_ID.format(self.dburl, collection_name, record_id, subcollection_name, record_id2)
        return url
    
    @Decorators.url_to_post
    def post_new_record_on_collection(self, collection_name, new_record, validate=True):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION.format(self.dburl, collection_name)
        if not validate:
            url += "?validate=false"
        return url

    @Decorators.url_to_post
    def post_new_record_on_subcollection(self, collection_name, record_id, subcollection_name, new_record, validate=True):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID_SUBCOLLECTION.format(self.dburl, collection_name, record_id, subcollection_name)
        if not validate:
            url += "?validate=false"
        return url

    @Decorators.url_to_put
    def put_existing_record_in_collection(self, collection_name, record_id, new_record):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url

    @Decorators.url_to_patch
    def patch_existing_record_in_collection(self, collection_name, record_id, new_record):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url
    
    @Decorators.url_to_delete
    def delete_record_by_id(self, collection_name, record_id):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION_ID.format(self.dburl, collection_name, record_id)
        return url
    
    @Decorators.url_to_delete
    def delete_record_by_query(self, collection_name, q={}):
        url = CollectionAPI.TEMPLATE_URL_COLLECTION.format(self.dburl, collection_name)
        url += "/*?q=" + str(q)
        url = url.replace("'", '"')
        return url