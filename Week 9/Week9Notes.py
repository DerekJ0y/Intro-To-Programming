with open("Week9/stuff.txt","r") as file:
    content=file.read()
    print(content)

with open('Week9/stuff.txt','r') as file:
    for line in file:
        print(line)