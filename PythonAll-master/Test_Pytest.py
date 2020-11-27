import requests
import json
import pytest


@pytest.fixture()
def fixturetest():
    print("------prints on method level------")
    print("=====scope=module----gives on onetime execution for the pytest run")
    print("-----yeild---afteer yeild statements will be executed as teardown method")


def test_pytesting(fixturetest):
    #res=requests.get("https://reqres.in/api/users?page=2")
    payload={
        "name": "morpheus",
        "job": "leader"
    }
    res=requests.post("https://reqres.in/api/users",data=payload)
    #print(res.json())
    print(json.dumps(res.json(),indent=4))
    resp=res.json()
def test_pytesting_get():
    res=requests.get("https://reqres.in/api/users?page=2")
    print(json.dumps(res.json(), indent=4))
    resp = res.json()

def test_pytesting_Failed():
    res=requests.get("https://reqres.in/api/users?page=2")
    #print(json.dumps(res.json(), indent=4))
    resp = res.json()
    assert resp["total_pages"]==5 ,7

@pytest.mark.set1
def test_Apiassert():
    res=requests.get("https://reqres.in/api/users?page=2")
    #print(json.dumps(res.json(), indent=4))
    resp = res.json()
    assert resp["total_pages"]==2 ,7
