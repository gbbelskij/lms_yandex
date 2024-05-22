from requests import delete


adress = input()
id_ = input()

delete("http://" + adress + "/users/" + id_)
