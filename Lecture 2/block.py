# for i in range (1, 13):
#     print ("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3 ))
#     print ("*" * 80)c


name = input ("Please enter your name: ")
age = int(input ("How old are you, {0}? ".format(name)))
print (age)

# if age >= 18:
#     print (" You're old enough to vote")
#     print (" Please put an X in the box")
# else: 
#     print ("please come back in {0} years".format(18 - age))
    
if age < 18: 
    print ("please come back in {0} years".format(18 - age))
elif age == 900:
    print ("Sorry, yoda you die in return of the jedi")
else:
    print (" You're old enough to vote")
    print (" Please put an X in the box")