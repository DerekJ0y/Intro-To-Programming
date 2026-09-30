for numbers in range(1, 6):
    print(numbers)

alive= input('Are you alive? ')
while alive != 'yes':
    input('Are you alive? ')

for groceries in ['apple', 'orange', 'pear', 'cereal', 'beef']:
    print(groceries)

for number in range(2, 8):
    print(number)
    square=number*number
    print(square)

for name in "Derek":
    print(name)

for number in range(1, 11):
    if number == 7:
        break

for x in range(1, 4):
    for y in range(1, 4): # it is outputting what it is because for every number the first loop is looping it has to loop then print the first and seacond set of looping numbers
        print(x,y)

