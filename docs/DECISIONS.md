In this file I will put my personal notes of why I made the decisions that I did.

The original project was complicated to understand, so I decided to make a simpler version with
improved readablitiy, more consisous.

# 1 - I decide to create a method to get response instead to try retrieve it in each method.
the reason is when I created the get response I can use it in all methods. avoinding repetition of code.
``` python
    # From
    def search_top_app(self):
            response = request.get('https://apkpure.com/top-apps')
            if response.status_code == 200:
                # DO SOMETHING
            else:
                # DO OTHER THING
    # To it
    def search_top_app(self):
            response = self.__get_response('https://apkpure.com/top-apps')
            # and the exception will be threated in the get_response method.
# To
```

# 2 - I decided to use `cloudscraper` cause the ApkPure website is protected by Cloudflare.
I used `cloudscraper` because it was easier for me to bypass its blocking.
The original project was using `requests`, but I had problems with it, like getting 403 status code due to the Cloudflare protection.
So I decided to use `cloudscraper`.

# 3 - From the original project all the scrap methods was inside the method, in this version I decided to put all the scrap in a separated file.
So in this way I can call it from any method, and avoid repetition of code. and more than it, The apkpure methods just be responsible to get the
html elements that there are the information that we need to extract, so `extractors` module will be used only for extracting this information.
then the extractors module through the it specified methods will return the information that we need.
# `From`
``` python

def search_top_app(self):
        # from
        def get_info(self, name: str) -> str:
        url = json.loads(self.search_top(name))["package_url"]
        html_obj = self.__helper(url)

        divs = html_obj.find("div", class_="detail_banner")
        title = divs.find("div", class_="title_link").get_text(strip=True)
        rating = divs.find("span", class_="rating").get_text(strip=True)
        date = divs.find("p", class_="date").text.strip()
        sdk_info = divs.find("p", class_="details_sdk")
        latest_version = sdk_info.contents[1].get_text(strip=True)
        developer = sdk_info.contents[3].get_text(strip=True)
        dl_btn = divs.find("a", class_="download_apk_news").attrs
        package_name = dl_btn["data-dt-package_name"]
        package_versioncode = dl_btn["data-dt-version_code"]
        download_link = dl_btn["href"]

        # Find the Description
        description = html_obj.find("div", class_="translate-content").get_text()

        # Older Versions
        versions = json.loads(self.get_versions(name))
        new = {
            "title": title,
            "rating": rating,
            "date": date,
            "latest_version": latest_version,
            "description": description,
            "developer": developer,
            "package_name": package_name,
            "package_versioncode": package_versioncode,
            "package_url": download_link,
            "older_versions": versions,
        }
        return json.dumps(new)

        
        

```
# `To it`
```python
    def get_info(self, name: str) -> dict:

            top_app = self.get_first_app_result(name)
            first_app_from_search : dict = json.loads(top_app) 

            info_url =  str(first_app_from_search.get('package_url')) + '/download'
            html_obj = self.__soup_factory(info_url)

            return json.dumps(
                scraper.extract_info_from_get_info(html_obj) | first_app_from_search,
                indent=4
                )

```

# 4 - Leave the user choose between the apk or xapk
Some apps has an apk and an xapk, so I decided to leave the user choose which one they want to download.
All the user need know before use this parameter is that the app has an xapk version, but the code threat it automatically if user use it wrong.


