import pytest
import requests

class TestApi:
    url=   'http://reqres.in/api/users/'

    def test_statuscode(self):
        response = requests.get(TestApi.url)
       # print("Responose" , response)
        assert 400>response.status_code>=200
# =============================================
    def test_email(self):
        response = requests.get(TestApi.url+'3')
        print("Responose" , response)
        dict1=response.json()
        print(dict1)
        exp='emma.wong@reqres.in'
        act=dict1['data']['email']
        assert exp==act
