import requests


URL = "https://restful-booker.herokuapp.com/booking"
headers = {
    "Content-Type": "application/json"
}
params = {
    "firstname": "Eric",
    "lastname": "Jackson",
    "bookingdates":
        {
            "checkin": "2022-10-17",
            "checkout": "2023-02-04"
        }
}

resp = requests.get(URL, headers=headers, params=params)

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Success' + '\n' + str(resp.content))
