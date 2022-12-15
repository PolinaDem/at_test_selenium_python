import requests
from requests.auth import HTTPDigestAuth

class TestDigestAuthentication:

    def test_digest_authentication(self):
        url = 'https://the-internet.herokuapp.com/digest_auth'

        response = requests.get(url, auth=HTTPDigestAuth('admin', 'admin'))
        print(response.status_code)
        assert response.status_code == 200
