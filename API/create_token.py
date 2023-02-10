import json
import requests


URL = "https://restful-booker.herokuapp.com/auth"
headers = {
    "Content-Type": "application/json"
}
params = {
    "username": "admin",
    "password": "password123"
}

resp = requests.post(URL, headers=headers, data=json.dumps(params))
tk = json.loads(resp.text)['token']

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('token: ' + str(tk))
    print('Success')
