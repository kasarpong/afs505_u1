name = 'Kobby sarpong'
age = 30
height = 68 #inches
weight = 210 #pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} and {hair}.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")


# Conversion factors
in_to_cm_convert_factor = 2.54
lb_kg_convert_factor = 0.453592

height_in_cm = height * in_to_cm_convert_factor
weight_in_kg = weight * lb_kg_convert_factor

print(f"My height in centimeters is {round(height_in_cm)}.")
print(f"My weight in kilograms is {round(weight_in_kg)}")
