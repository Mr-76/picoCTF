import base64
string = input("name the string to decode ")


for times in range(100):
    string = base64.standard_b64decode(string)
    print("decoded string")
    print(string)



