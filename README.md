# Apk Pure Api

An API for interacting with the APK Pure website, allowing you to search for apps, retrieve app information, and download apps programmatically.

## Features

- **Search for Apps**: Find apps on APK Pure by querying their name or keywords.
- **Get App Info**: Retrieve detailed information about a specific app, including version, developer, ratings, and more.
- **Download App**: Programmatically download the APK files of the apps.

## Getting Started

### Prerequisites

- Python 3.7+
- `requests` library
- `beautifulsoup4` library
- `tqdm` library
- `cloudscraper` library

### Installation

1. Clone the repository:

```sh
git clone https://github.com/thawancomt/apkpureAPI.git
cd apkpure
```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```sh
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

4. Install the required libraries:

   ```sh
   pip install -r requirements.txt
   ```

   </details>

### Usage

Here's a quick example of how to use the `ApkPure` class:

```python
from apkpure.apkpure import ApkPure

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
```

#### Class: `ApkPure`

A class to interact with ApkPure for searching apps, retrieving app information, and downloading APK files.

<details>
  <summary><code>__init__(verbose : bool = True) -> None</code></summary>
  
  Initialize the `ApkPure`
</details>

<details>
  <summary><code>search_top(name: str) -> str</code></summary>
  
  Search for the top result of an app on APK Pure.

- **Parameters**:
  - `name` (str): The name of the app to search for.
- **Returns**:
  - `str`: A JSON string containing details of the top search result.

</details>

<details>
  <summary><code>search_all(name: str) -> str</code></summary>
  
  Search for all results of an app on APK Pure.

- **Parameters**:
  - `name` (str): The name of the app to search for.
- **Returns**:
  - `str`: A JSON string containing details of all search results.

</details>

<details>
  <summary><code>get_versions(name: str) -> str</code></summary>
  
  Retrieve all available versions of the specified app.

- **Parameters**:
  - `name` (str): The name of the app.
- **Returns**:
  - `str`: A JSON string containing the details of all available versions.

</details>

<details>
  <summary><code>get_info(name: str) -> str</code></summary>
  
  Retrieve detailed information about the specified app.

- **Parameters**:
  - `name` (str): The name of the app.
- **Returns**:
  - `str`: A JSON string containing detailed information about the app.

</details>

<details>
  <summary><code>download(name: str, version: str = "") -> str | None</code></summary>
  
  Download the specified version of the app. If no version is specified, download the latest version.

- **Parameters**:
  - `name` (str): The name of the app.
  - `version` (str, optional): The version of the app to download. Defaults to the latest version.
- **Returns**:
  - `str | None`: The real path to the downloaded APK file, or `None` if the version is invalid.

</details>

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please make sure to update tests as appropriate.

## Contact

If you have any questions, suggestions, or feedback, feel free to contact me:

- GitHub: [anishomsy](https://github.com/anishomsy)

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
