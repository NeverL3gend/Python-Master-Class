# declared a variable age with the value of 24
age = 24
# converted an integer into a string
#format is basically doing is formating the substitution and converting it into a string.
# substitution is identified by the curly brackets within the string
print ("My age is {0} years".format(age))


#explaining what is happening:
####
# In our code, we used 8 replacement fields - numbered from 0-7
# These are replaced with the values in the parentheses after .format
# These first value goes into {0}, the second into {1} and so on
# #

print ("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
       .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print ("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print ("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec:{2}"
       .format(28,30,31)) 

print ()

print (""" 
       Jan: {2}
       Feb: {0}
       Mar: {2}
       Apr: {1}
       May: {2}
       Jun: {1}
       Jul: {2}
       Sep: {1}
       Oct: {2}
       Nov: {1}
       Dec: {2}
       """.format(28,30,31))