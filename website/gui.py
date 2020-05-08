import requests
import json
BASE_URL = 'http://localhost:1337'


def send_score(name, score):
    data_obj = {
        'name': name,
        'score': score,
    }
    headers = {
        'content-type': 'application/json'
    }
    r = requests.post(BASE_URL + '/Api/Score/AddScore', data=json.dumps(data_obj), headers=headers)
    print(r.status_code)
    print(r.text)
    return r


if __name__ == "__main__":
    username = 'amy'
    score = 20
    send_score(username, score)
