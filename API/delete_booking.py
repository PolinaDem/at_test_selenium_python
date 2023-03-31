import requests
import create_token


URL = "https://restful-booker.herokuapp.com/booking"
aut = "token=" + create_token.tk

headers = {
    "Content-Type": "application/json",
    "Cookie": aut
}

id = 1
resp = requests.delete(f"{URL}/{id}", headers=headers)

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Success' + "The book was deleted")
