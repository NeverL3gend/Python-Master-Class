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
       .format(31, "Jan", "Mar", "May", "jul", "aug", "oct", "dec"))
