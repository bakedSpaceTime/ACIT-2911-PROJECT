"""
Pandemic Run
Course: ACIT 2911, Agile Development
Authors:
- Jaskaran Saini, A01055847
- Jeffery Law, A00864331
- Ming Yen Hsieh, A01170219
- Tushya Iyer, A01023434
- Shivar Pillay, A01079978
- Shivam Patel, A01185250
"""

import json
import requests

BASE_URL = 'http://rocky-river-43342.herokuapp.com/Api/Score/AddScore'
# BASE_URL = 'http://localhost:1337/Api/Score/AddScore'


def send_score(name, score):
    data_obj = {
        'name': name,
        'score': score
    }
    headers = {
        'content-type': 'application/json'
    }
    r = requests.post(BASE_URL, data=json.dumps(data_obj), headers=headers)
    print(r)
    print(r.text)
    return r

