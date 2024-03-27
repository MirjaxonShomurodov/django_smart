from tinydb import TinyDB
import requests
db = TinyDB('db.json',indent=4)
tiem = db.table('Huawei')
def get_brend():
    return  tiem.all()

def send_data():
    url = "http://127.0.0.1:8000/api/add/"
    for item in get_brend():
        r = requests.post(url,json=item)
        print(r.status_code)
    return "OK"

print(send_data())
