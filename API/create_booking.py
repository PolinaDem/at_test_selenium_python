import requests
import json


URL = "https://restful-booker.herokuapp.com/booking"
headers = {
    "Content-Type": "application/json"
}
params = {
    "firstname": "Jimmy",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-02",
        "checkout": "2019-01-02"
    },
    "additionalneeds": "Test"
}

resp = requests.post(URL, headers=headers, data=json.dumps(params))

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Success' + '\n' + str(resp.content))


# Check booking was created
resp = resp.json()
id = resp['bookingid']
print("id =", id)

resp = requests.get(f"{URL}/{id}")

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Success' + '\n' + str(resp.json()))
