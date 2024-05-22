from sys import stdout

arr = []

def modern_print(string):
    if string not in arr:
        arr.append(string)
        stdout.write(string)
