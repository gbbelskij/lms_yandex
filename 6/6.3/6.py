from requests import get


adress = input()
users = []
for i in get("http://" + adress + "/users").json():
    users.append(i["last_name"] + " " + i["first_name"])
print(*sorted(users), sep='\n')
