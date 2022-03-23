#Challenge

# Write a small program to ask for a name and an age.a

# when both values have been entered, check if the person is the right age to go on an 18-30 
# holiday(they must be over 18 and under 31)

# If they are, Welcome them to the holiday, otherwise print a polite message refusing their entry.

# Our programs expect valid input. 


name = input("what is your name?: ")
age = int(input("How old are you?: "))

if age <= 18 < 31:
    print ("Welcome, hope you have fun at the club, {0}".format(name))
else:
    print("Sorry you're not allowed to enter the club")
