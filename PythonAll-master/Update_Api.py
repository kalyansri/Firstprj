import requests
import json

#res=requests.get("https://reqres.in/api/users?page=2")
payload={
    "name": "morpheus",
    "job": "Pega developer"
}
res=requests.put("https://reqres.in/api/users/2",data=payload)
#print(res.json())
print(json.dumps(res.json(),indent=4))
resp=res.json()
