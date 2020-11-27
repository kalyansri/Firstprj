import requests
import json

#res=requests.get("https://reqres.in/api/users?page=2")
params={'page':2}
res=requests.get("https://reqres.in/api/users",params=params)
#print(res.json())
print(json.dumps(res.json(),indent=4))
resp=res.json()

#import ipdb;ipdb.set_trace()

fn=[d["first_name"] for d in resp["data"]]
print(fn)