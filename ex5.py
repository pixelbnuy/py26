# more variables and printing

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# everytime you put " around a piece of text you are making a string
# you embed variables inside a string by using a special {} and put the variable inside
# the little f before characters  is to format the string
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} I get {total}.")