Here is the "How to Use" ApkPure API:

**Introduction**

The ApkPure API provides a simple and convenient way to interact with the ApkPure website, allowing you to search for apps, retrieve information about specific apps, and even download APKs. This guide will walk you through how to use the API.

**Getting Started**

To get started, you'll need to import the `ApkPure` class from the `apkpure.py` file:
```python
from apkpure.apkpure import ApkPure
```
Create an instance of the `ApkPure` class:
```python
API = ApkPure()
```

**Searching for Apps**

To search for apps, use the `get_first_app_result()` method and pass in the name of the app you're interested in:
```python
top_result = API.get_first_app_result('App Name')
```
This will return the information about the first result from the search query.

**Retrieving All App Results**

To retrieve all results from the search query, use the `get_all_apps_results()` method and pass in the name of the app you're interested in:
```python
all_results = API.get_all_apps_results('App Name')
```
This will return a list of dictionaries containing information about each app result.

**Retrieving App Information**

To retrieve detailed information about a specific app, use the `get_info()` method and pass in the name of the app you're interested in:
```python
app_info = API.get_info('App Name')
```
This will return a dictionary containing information about the app, including its title, developer, rating, download count, latest update, etc.

**Retrieving App Versions**

To retrieve all versions of an app, use the `get_versions()` method and pass in the name of the app you're interested in:
```python
versions = API.get_versions('App Name')
```
This will return a list of dictionaries containing information about each version of the app.

**Downloading Apps**

To download an APK or XAPK, use the `download()` method and pass in the name of the app you're interested in:
```python
API.download('App Name')
```
You can also specify a specific version to download by passing in the `version` parameter and the `xapk` for true to download the xapk file:
```python
API.download('App Name', '1.0.2', xapk=False)  # Download version 1.0.2
# or if you want download a xapk
API.download('App Name', '1.0.2', xapk=True)  # Download version 1.0.2 as xapk if it are available 
```

**Tips and Tricks**

* Make sure to check the API documentation for any rate limits or usage guidelines.
* You can use the `__check_name()` method to validate the app name before making a request.
* The `__soup_factory()` method is used to create a BeautifulSoup object from an HTML response.

That's it! With these simple steps, you should be able to get started with using the ApkPure API. Happy coding!
