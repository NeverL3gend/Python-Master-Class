# letters = "abcdefghijklmnopqrstuvwxyz"

# backwards  = letters [25:0:-1] #expected output zyxw ....
# backwards2 = letters [25::-1]
# backwards3 = letters [::-1]
# print (backwards)
# print (backwards2)

# Challenge 
####
#
# Create a slice that produces the characters qpo
# slice the string to produce edcba
# slice the string to prodice the last 8 characters, in revers order#

#use letters for this challenge:
letters = "abcdefghijklmnopqrstuvwxyz"

#Challenge 1
# Create a slice that produces the characters qpo
slice = letters [16:13:-1] # 16 is the starting point, 13 is the stopping point, we're stepping -1
print (slice)

#Challenged 2
#slice the string to produce edcba
slice2 = letters [4::-1] # starting point is e, then we defaulted back to the start of the string which is "a" then stepping back -1
print (slice2)

#Challenge 3
# slice the string to produce the last 8 charactes in reverse order
slice3 = letters [25:17:-1] #OR use [:-9:-1]
print(slice3)