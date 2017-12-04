# 3. Write comments above each of the variable assignments.

# This statement assigns the value of 100 to the variable cars
cars = 100
# This statement assigns the value of 4.0 to the variable space_in_a_car
space_in_a_car = 4.0
# This statement assigns the value of 30 to the variable drivers
drivers = 30
# This statement assigns the value of 90 to the variable passengers
passengers = 90
# This statement subtracts the value stored in drivers from the value stored in cars and stores the result in cars_not_driven
cars_not_driven = cars - drivers
# This statement assigns the value stored in drivers to cars_driven
cars_driven = drivers
# This statement multiplies the value stored in cars_driven by the value stored in space_in_a_car and stores the result in carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# This statement divides the value stored in passengers by the value stored in cars_driven and stores the result in average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
     "in each car.")