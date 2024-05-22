from requests import post
from json import dumps


adress = input()
user = {
    "username": input(),
    "last_name": input(),
    "first_name": input(),
    "email": input(),
}
response2 = post("http://" + adress + "/users", user)
