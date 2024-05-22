from requests import get
from sys import stdin


adress = input()
id_ = input()
text = ''.join(i for i in stdin)
try:
    user = get("http://" + adress + "/users/" + id_).json()
except ValueError:
    print("Пользователь не найден")
else:
    for i in user:
        text = text.replace("{" + i + "}", str(user[i]))
print(text)
