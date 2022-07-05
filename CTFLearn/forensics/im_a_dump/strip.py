with open('text2.txt','r') as file:
    file = file.readlines()
    tuple_of_char = ('Ø','H','E','Ð','à')
    string = file[0]
    for char in tuple_of_char:
        string = string.replace(char,"")
    print(string)
