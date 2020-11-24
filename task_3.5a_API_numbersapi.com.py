import requests
import sys

api_url = "http://numbersapi.com/"
api_url_end = "/math"
params = {"json": "true"}
for number in sys.stdin:
    number = number.rstrip()
    res = requests.get(api_url + number + api_url_end, params=params)
    data = res.json()
    if data["found"] is True:
        print("Interesting")
    elif data["found"] is False:
        print("Boring")
