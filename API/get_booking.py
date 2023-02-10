import requests


URL = "https://restful-booker.herokuapp.com/booking"
headers = {
    "Accept": "application/json"
}
id = 1
resp = requests.get(f"{URL}/{id}")

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Success' + '\n' + str(resp.json()))
