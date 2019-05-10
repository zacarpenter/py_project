#variable named formatter with a string that includes {} to be formatted
formatter = "{} {} {} {}"

#printing the variable formatter while also formatting it to use 1, 2, 3, 4
print(formatter.format(1, 2, 3, 4))
#
print(formatter.format('one', 'two', 'three', 'four'))
#printing formatter while formatting the {} to print Booleans
print(formatter.format(True, False, True, False))
#printing formatter while formatting the {} to print the variable formatter
print(formatter.format(formatter, formatter, formatter, formatter)) #should print 12 {}
#printing formatter while formatting {} to produce the strings
print(formatter.format(
    "Piper",
    "is the cutest",
    "Watty",
    "has a stinky tongue"
))

#the multi line approach is just meant to confuse
#as suspected, this did not print the strings on separate lines
#because the variable formatter was set a one line strings
