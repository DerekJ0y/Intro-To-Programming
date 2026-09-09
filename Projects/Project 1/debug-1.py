# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.

total = 0
num1 = float(input("What's the first number? >"))
num2 = float(input("What's the second number? >")) # num1,2,and 3 needed to be converted to strings to be added together
num3 = float(input("What's the third number? >"))
total = num1+num2+num3 # instaed of just changing the total variable the 3 num variables needed to get added together
print(f"Total is: {total}")