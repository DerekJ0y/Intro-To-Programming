# grocery list
with open('Week 9/file lab/Challenge/Grocery list.txt','r') as file:
    for line in file:
        print(line)


item= input('please add an item that you want me to grab: ')
with open('Week 9/file lab/Challenge/Grocery list.txt','a') as file:
    file.write('\n' +item)
    print('Here is the grocery list')


with open('Week 9/file lab/Challenge/Grocery list.txt','r') as file:
    for line in file:
        print(line)