# changed the value of "day" from Monday to Saturday
day = "Friday"
# No value has been changed
temperature = 30
# raining is set to true meaning it is raining
raining = False

# in order to print "go swimming" each of the conditions need to equal true
# changed and not -> or not
# 
if (day == "Saturday" and temperature > 27) or not raining:
    print ("go swimming")
else:
    print ("Learn Python")