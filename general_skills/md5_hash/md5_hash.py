import hashlib

string = input("ur data ")

string = bytes(string,"utf-8")
print(string)

hashed = hashlib.md5(string)
print(hashed.digest())#nromal one not hex thats what we need


print(hashed.hexdigest())
