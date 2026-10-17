Input=float(input("please give me a number to calculate: "))
number= Input
while number !=0:
    minus=float(input(f'give me a number to slowly get {number} to zero: '))
    number=number-minus
print("congrats you made it to zero")