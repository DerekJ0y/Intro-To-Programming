#week 10
#function is a named set of instructions
#functions let us write code ad then reuse it
#define a function: create a function using define
#call a function: running a function by using its name in ""
#parameter: placeholder value in a function
#Argument: a real value you pass in with call function


# define a function
# def say_hello():
#     print("hello")
# call the function
# say_hello()


#aruments and paramaters
#function is going to greet me by name 
#function is going to be called greet
# def greet(name):
#     #name is a parameter
#     #print out hello {name}
#     print(f'hello, {name}')
# call my function and it is going to say
# greet("Derek")
# parameters ar like blanks and arguments fill them

# functions a reusable code
# Orgenization, allows our program to become readable
# breaking big problems into small parts

# print('welcome')
# print('pick an option')
# print('goodbye')


# def show_menu():
#     print('welcome')
#     print('pick an option')
#     print('goodbye')
# show_menu()

# def hello_world():
#     print('hello')

# def hello_return():
#     return "hello world"

# print if for the user return is for the program

# msg=hello_return()
# print(msg)

# calculatro program that uses 2 functions

# def calc(num1,num2):
#     operator=input('choose an operator: +,-,*,?')

# fake loop
# a function can call itself
# behaves like a loop

def play_again():
    question=input('do you want to play again: y/n' ).lower
    if question=='y':
        play_again()
    else:
        print('goodbye')
