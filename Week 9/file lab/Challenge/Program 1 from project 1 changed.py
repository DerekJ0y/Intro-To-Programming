# grocery list
item= input('what item would you like to add to the list: ')
with open('Week 9/file lab/Challenge/Grocery list.txt','a') as file:
    file.write("/n" +item)
    print('Here is the grocery list')
with open('Week 9/file lab/Challenge/Grocery list.txt','r') as file:
    for line in file:
        print(line)