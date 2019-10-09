cars = 100
#changed the floating point 4.0 to 4
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#fixed cars_driven from "cars_not_driven"

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


#Traceback (most recetn call last):
# File "ex4.py", line 8, in <module>
#   average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined

#In other words the NameError was a result of the the variable being named 'car_pool_capacity'
#Not being named 'carpool_capacity' like the original variable
#There was no value set for 'car_pool_capacity'
