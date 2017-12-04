# 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_height_cm = round(my_height * 2.54 )# 2.54 centimeters in an inch.
my_weight = 180 # lbs
my_weight_kg = round(my_weight * 0.453592) # 0.453592 kilograms in a pound
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"That's {my_height_cm} centimeters.")
print(f"He's {my_weight} pounds heavy.")
print(f"That's {my_weight_kg} kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usuall {my_teeth} depending on the coffe.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")