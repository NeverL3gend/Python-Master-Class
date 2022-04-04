number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    # isnumeric() will return true if the character is a number else it is false
    # but we used if not to make sure that we're only adding non-numberic characters
    if not char.isnumeric():
        separators = separators + char
print (separators)

values = "".join(char if char not in separators else " " for char in number).split()
print (sum([int(val) for val in values]))