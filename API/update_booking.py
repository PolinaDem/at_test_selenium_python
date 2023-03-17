import requests
import json
import create_token


URL = "https://restful-booker.herokuapp.com/booking"
aut = "token=" + create_token.tk
headers = {
    "Content-Type": "application/json",
    "Cookie": aut
}
params = {
    "firstname": "J1am2e11s",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Test Update"
}

id = 1
resp = requests.put(f"{URL}/{id}", headers=headers, data=json.dumps(params))

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Success' + '\n' + str(resp.content))
