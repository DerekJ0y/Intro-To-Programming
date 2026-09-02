int=45
float=2.5
# Can you still do math with a float and integer, or can you only do math with one at a time?: YES
int= input('give me a whole number between 1 and 10: ')
float= input('Give me a decimal number between 1 and 2: ')

# What is a string?: A STRING IS A COLLECTION OF CHARACTERS THAT ARE EITHER WORD OR LETTERS THAT ARE USUALLY IN QUOTATION MARKS

word= 'Phil'
hello=f'hello {word}'
print(hello)
print(word[0]) 
llo=hello[2:5]
print(llo)

# What type of data do you think a list can contain? A LIST CAN HOLD ANY TYPE OF DATA OF THE TYPES WE KNOW IT CAN HOLD STRINGS, INTEGERS, FLOATS, AND VARIABLES

games=['Fallout 4', 'Halo Reach', 'Rocket League']
games.append('Dota 2')
print(games) # What happens? IT PRINTS THE WHOLE LIST INCLUDING DOTA 2
games.remove('Halo Reach')
print(games)
# SEPERATED FOR LENGTH PURPOSES
# In this lab I learned a few thing I did not know before. I learned in this lab is that you don't have to print the characters you indexed for right away. 
# I learned that you can use a caracter when splicing that is out side the string langth to get the last character of a string. Finally the last thing 
# I learned from this lab is that even if I know somthing if I don't how it is phased when typed out I get very confused.