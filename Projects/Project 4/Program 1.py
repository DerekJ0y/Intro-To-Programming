import random # creates randon choice from the txt file

def choose_number():
    with open('C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Project 4/numbers for program 1.txt', 'r') as file: # Did not allow a relotive path
        number_list = file.read().split()  # Took insperation fron the hangman debug lab
    return int(random.choice(number_list)) # picks a number at ranbom
number=choose_number()
while number != 0:
    if number > 0: # modified version of program 2 fron project 3
        minus=float(input(f'give me a number to get {number} down to zero: ')) # has the user give a number to try to get the random number to 0
        number=number-minus
    elif number < 0:
        plus=float(input(f'give me a number to get {number} back up to zero: ')) # if the number overshoots 0
        number=number+plus

print("congrats you made it to zero")