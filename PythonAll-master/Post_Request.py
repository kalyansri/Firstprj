import requests
import json

#res=requests.get("https://reqres.in/api/users?page=2")
payload={
    "name": "morpheus",
    "job": "leader"
}
res=requests.post("https://reqres.in/api/users",data=payload)
#print(res.json())
print(json.dumps(res.json(),indent=4))
resp=res.json()
