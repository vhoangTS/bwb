import requests
from server import app

if __name__ == '__main__':

    # Request body
    payload = {
        'username': 'admin',
        'password': 'foo',
        'keyword': 'bosch',
        'nr_results': 10}

    response = requests.post("http://127.0.0.1:5000/search-request",
                             json=payload,
                             headers={'Content-type': 'application/json',
                                      'accept': 'application/json'})
    print(response.status_code)
    print(response.json())
