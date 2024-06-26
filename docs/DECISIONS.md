In this file I will put my personal notes of why I made the decisions that I did.

The original project was complicated to understand, so I decided to make a simpler version with
improved readablitiy, more consisous.

# 1 - I decide to create a method to get response instead to try retrieve it in each method.
the reason is when I created the get response I can use it in all methods. avoinding repetition of code.
`` python
    # From
    def search_top_app(self):
            response = self.get_response('https://apkpure.com/top-apps')
            if response.status_code == 200:
                # DO SOMETHING
            else:
                # DO OTHER THING
    # To it
    def search_top_app(self):
            response = self.__get_response('https://apkpure.com/top-apps')
            # and the exception will be threated in the get_response method.
# To
``

# 2 - I decided to use `cloudscraper` cause the ApkPure website is protected by Cloudflare.
I used `cloudscraper` because it was easier for me to bypass its blocking.
The original project was using requests, but I had problems with it, like getting 403 status code due to the Cloudflare protection.
So I decided to use `cloudscraper`.

# 3 - From the original project all the scrap methods was inside the method, in this version I decided to put all the scrap in a separated file.
So in this way I can call it from any method, and avoid repetition of code. and more than it, The apkpure methods just be responsible to get the
html elements that there are the information that we need to extract, so `extractors` module will be used only for extracting this information.
then the extractors module through the it specified methods will return the information that we need.

# 4 - Leave the user choose between the apk or xapk
Some apps has an apk and an xapk, so I decided to leave the user choose which one they want to download.
All the user need know before use this parameter is that the app has an xapk version, but the code threat it automatically if user use it wrong.


