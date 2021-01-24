# assigning value to variable
types_of_people = 10

# assigning string with embedded variable to x
x = f"There are {types_of_people} types of people."

# assigning strings to variables
binary = "binary"
do_not = "don't"

# assigning strings with embedded variables to y
y = f"Those who know {binary} and those who {do_not}."

# printing values of variables x and y
print(x)
print(y)

# printing strings with embedded variables
print(f"I said: {x}")
print(f"I also said '{y}'")

# assigning boolean value and strings to variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# using printing string with variable embedded with .format function
print(joke_evaluation.format(hilarious))

# assigning string to variables
w = "This is the left side of ..."
e = "a string with a right side."

# joining strings with addition
print(w + e)
