# Python provides several ways to repeat a block of code - things like:
# > for loops
# > while loops
# List comprehensions and generator expressions
# 
# A "for" loop works by iterating over some set of values.
# It assigns each of the values, one by one, to one or more variables
# It then executes a block of code once for each value.
# 
# The set of values comes from a "sequence, or some other iterable object."
# We've seen one sequence type - the string type. 
# An "iterable" object is anything that can be iterated over. That means a "sequence" is also an iterable
# In simple terms, you can use it with a "for" loop, then it's "iterable"
# # 


# parrot = "Norwegian Blue"

# for character in parrot:
#     print (character)

number = "9,223;372:036 854, 775;807"
separators = ""

for char in number:
    # isnumeric(): checks if all the characrs in the text are numeric
    if not char.isnumeric():
        separators = separators + char
print (separators)

values = "".join(char if char not in separators else " " for char in number).split()
print ([int(val) for val in values])