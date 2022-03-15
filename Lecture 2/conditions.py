age = int(input("How old are you? "))
##
# Notes:
# So what this is saying is that if your age is greater than or equal to 16 (age >= 16) and if you're younger than or equal to the age of 65 (age <= 65).
# print message
# if age >= 16 and age <= 65:

if 16 <= age <= 65:
    print ("Have a good day at work.")
else: 
    print ("enjoy your free time.")
    
print ("-" * 80)

if age < 16 or age > 65:
    print ("enjoy your free time")
else: 
    print ("Have a good day at work")