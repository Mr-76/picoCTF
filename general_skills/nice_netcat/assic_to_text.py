#coding : UTF-8

with open('text.txt','r') as file:
    file_read = file.read()
    file_read = file_read.split(" ")
    file_read[-1] = '0'
    for i in file_read:
        i = i.strip("\n")
        i = int(i)
        i = chr(i)
        print(i,end="")

    print(file_read)
