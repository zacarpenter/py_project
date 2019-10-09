#variable and its value
types_of_people = 10
#variable value is set to an f-string
x = f"There are {types_of_people} types of people."

#variable value is a string
binary = "binary"
#variable value is a string
do_not = "don't"
#variable value is set to an f-string with two varibles included
y = f"Those who know {binary} and those who {do_not}."

#printing the two previous variables that includes f-strings
print(x)
print(y)

#printing an f-string with a variable (that also contains an f-string with variable)
print(f"I said: {x}")
#printing an f-string with a variable (that also contains an f-string)
print(f"I also said: {y}")


#hilarious = false
#doesn't work because I didn't capitalize False
hilarious = False
#variable is set to a string that includes a Boolean
joke_evaluation = "Isn't that joke so funny?! {}"

#prints the variable (string) and formats the variable (Boolean)
print(joke_evaluation.format(hilarious))

#variable is a string
w = "This is the left side of..."
#variable is a string
e = "a string with a right side."

#prints the variables (strings) w and e on the same line
print(w + e)
