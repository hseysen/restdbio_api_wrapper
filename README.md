# Restdb.io API Wrapper

This package is an API Wrapper for the website [restdb.io](https://restdb.io), which allows for online databases. The API calls to the databases rely on the Rest API, I just made python classes and methods to make things easier to work with. The package is still in development stage, and I have so far only been able to implement a `CollectionAPI` class, along with custom decorators and exceptions.

## Installation

Haven't uploaded/deployed to PyPI yet.

## Usage

Using the package to connect to your database on [restdb.io](https://restdb.io) is pretty straightforward. First of all, you need your **dburl** and **x-apikey**. **dburl** is mostly the same as your database name in the [Databases dashboard](https://restdb.io/account/databases/). Head over to the following link to see your api key:
`https://restdb.io/account/databases/<dburl>/api`  
Then, put the following line in your code:
```python
from restdbio_api_wrapper import Connection
```
Proceed to creating a `Connection` object:
```python
database_connection = Connection(<dburl>, <x-apikey>)
```

Everything will be set up for you after this. You can access the `CollectionAPI` object automatically created within the `Connection` object using the `.collection_api` attribute. Through your `CollectionAPI` object, you are able to make API calls directed at your collection in your database. For example:

```python
result = database_connection.collection_api.get_records_from_collection("demo_collection", q={"first_name": "Jack"})
```

You can of course, use different methods, customize your queries, use additional parameters like `max`, `skip`, `filter`, `groupby`, `aggregate` and so on. Issue the following line to see all methods available:

```python
help(database_connection.collection_api)
```

## Contributing
As I've said earlier, this package is still in development stage. Should you have any issues or ideas, feel free to contribute. You can also e-mail me:
<hesenisgenderli999@gmail.com>
