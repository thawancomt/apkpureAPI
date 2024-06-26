"""
This file is to support you to use the apkpure api
"""

# Import the API
from apkpure.apkpure import ApkPure

API = ApkPure()

# Get the first result from app
top_result = API.get_first_app_result(name='App Name')

# Get all apps from result
all_results = API.get_all_apps_results(name='App Name')

# Get info from an app
app_info = API.get_info(name='App Name')

# Get the versions of an app
versions = API.get_versions(name='App Name')

# Downlaod an app, you can pass a version and also the type of file between apk and xapk
# version and xapk are optional parameters
API.download(name='App Name', version='1.1.1', xapk=True)