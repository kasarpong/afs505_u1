# Assigning values to variables

# of cars
cars = 100

# Available seating
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# Estimating averaf
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars, "car available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
