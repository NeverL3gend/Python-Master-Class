string1 = "he's " 
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print (string1 + string2 + string3 + string4 + string5)

print ("he's " "probably " "pining " "for the " "fjords" )

# this is going to repeat how many times hello will be printed
print ("Hello " * 5)
#since 5 + 4 is parentheses, it evaluates to 9 so Hell should print 9 times
print ("Hello " * (5 + 4))
# should print Hello 5 times then append the string 4 to it
# Append means to add something to the existing item.
print ("Hello " * 5 + "4")

today = "friday"
print ("day" in today)      # True
print ("fri" in today)      # true
print ("thur" in today)     # false
print ("parrot" in "fjord") # false
