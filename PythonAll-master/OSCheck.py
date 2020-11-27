import os

import requests

path=os.getcwd()
print(path)

# os.mkdir("sagdir")
# os.rename("sagdir","newdir")
print(os.getenv("path"))
# environ is a variable which have all set of data in python os file
# print(os.environ)

payload={'page':2, 'count':25}
url="https://httpbin.org/get"
response=requests.get(url, params=payload)
print(response.json())
url_post="https://httpbin.org/post"


pay={'username':'sagar','password':"testing"}
r=requests.post(url_post, data=pay)
print(r.text)