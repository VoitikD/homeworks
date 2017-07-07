# Requests
import requests




def get_json():
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    print(r.status_code)
    print(r.headers)
    print(r.content)

get_json()s