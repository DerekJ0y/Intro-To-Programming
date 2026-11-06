import random

def choose_number():
    with open("Intro-To-Programming\Projects\Project 4\numbers for program 1.txt", "r") as file:
        number_list = file.read().split()
    return int(random.choice(number_list))
number=choose_number()
while number != 0:
    if number > 0:
        minus=int(input(f'give me a number to slowly get {number} to zero: '))
        number=number-minus
    elif number < 0:
        plus=int(input(f'give me a number to get {number} back up to zero: '))
        number=number+plus

print("congrats you made it to zero")