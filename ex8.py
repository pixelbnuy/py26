# Printing, printing

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# using function to turn the formatter variable into other strings
# formatter.format(...) means:
# 1. Take the formatter string defined on line 3
# 2. Call its format function, which is similar to telling it to do a command line command named format
# 3. Pass to format four arguments, which match up with the four {}s in the formatter variable
#    This is like passing arguments to the command line command format
# 4. The result of calling format on formatter is a new straing that has the {} replaced with the four variables
#    This is what print is printing out 
