part_1=input('choose a first number: ') # modified program of part 2 of project 0
part_2=input('choose a number that will be added subracted multiplied to and divided from the first number: ') # Choose 2 numbers that will be added, subracted, multiplied, and divided together

def add(add_part_1, add_part_2):
    add_part_1=int(add_part_1)
    add_part_2=int(add_part_2) # change the 2 strings into floats
    ad=add_part_1+add_part_2 # adds the floats
    print(F'your numbers you chose added into {ad}')


def subtract(sub_part_1, sub_part_2):
    sub_part_1=int(sub_part_1)
    sub_part_2=int(sub_part_2) # change the 2 strings into floats
    sub=sub_part_1-sub_part_2 # subtracts the floats
    print(F'your numbers you chose subtracted into {sub}')


def multiply(mult_part_1, mult_part_2):
    mult_part_1=float(mult_part_1)
    mult_part_2=float(mult_part_2) # change the 2 strings into floats
    mult=mult_part_1*mult_part_2 # multiplies the floats
    print(F'your numbers you chose multiplied into {mult}')

def divide(div_part1, div_part2):
    div_part1=float(div_part1)
    div_part2=float(div_part2) # change the 2 strings into floats
    div=div_part1/div_part2 # divides the floads
    print(F'your numbers you chose divided into {div}')
add(part_1, part_2)
subtract(part_1, part_2)
multiply(part_1, part_1)
divide(part_1, part_2)