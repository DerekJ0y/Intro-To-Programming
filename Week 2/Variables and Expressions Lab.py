# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.

vegi1="Carret"
vegi2="Lettuce"
vegi3="Raddish"
fruit1="Strawberry"
# Then print your variables.
print(f"my grocery list contains the following produce items:{vegi1},{vegi2},{vegi3},{fruit1}")

# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
vegi1="Rudibega"
# After you've done this, try to print your variables in string using f-strings.
print(f"my grocery list contains the following produce items:{vegi1},{vegi2},{vegi3},{fruit1}")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
x=7*7
print(x)

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp
x= 77
y=29
z=11
a=0
math=x+y-z*a
print(math)
# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
first="Derek "
last="Joy"
Full=first+last
print(Full)
# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
        #find the number of items on a shelf need to be stacked if the the shelf holds 35 item and there are 12 left
Total_items=35
Items_left=12
items_needed=Total_items-Items_left
print(f"there are {items_needed} items that need to be stacked")

# Upload this to Canvas under the Variable and Expressions Lab assignment.