#defining function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of cracker!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

#ways of assigning values to functions
#direct method
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#variable method
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#variant of direct method, using arithmetic
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#combination of variable and maths methods
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

#study drill code
def mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers)/ len(numbers)

#testing my function
#1st way of running my function
average = mean([23, 24, 28, 30, 45, 20, 22, 29])
print(f"The average is {average}")

#prices of car
sedan_prices = [23000, 24000, 45000, 36000, 30000]
suv_prices = [40,000, 29000, 39000, 50000, 90000]

#2nd way of running my functions
average_sedan = mean(sedan_prices)
average_suv = mean(suv_prices)
print(f"The average price of a sedan is ${round(average_sedan)}) and ${round(average_suv)}) for an SUV")

#3rd way of running function
average_car = mean(sedan_prices + suv_prices)
print(f"The average price of a car is ${round(average_car)}")
