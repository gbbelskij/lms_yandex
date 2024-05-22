from json import dumps
from requests import put
from sys import stdin


adress = input()
id_ = input()
change = [i.rstrip('\n').split('=') for i in stdin]
data = {}
for i in change:
    data[i[0]] = i[1]
response = put("http://" + adress + "/users/" + id_, dumps(data))
