import requests
import json
from requests.structures import CaseInsensitiveDict

port = 5001
path = '/sport/'
data = {}

headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/json'
test = requests.put( f'http://localhost:{port}{path}', headers=headers, data=json.dumps(data))
a = (test.status_code == 200, json.loads(test.text))
print(a)