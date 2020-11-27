import requests

 #url="http://dummy.restapiexample.com/api/v1/employees"

#json_response=requests.get(url).json()

#print(json_response)

url="	http://dummy.restapiexample.com/api/v1/employee/"
id=input("Employee ID :")

C_url=url + id

json_response=requests.get(url).json()
print(json_response)