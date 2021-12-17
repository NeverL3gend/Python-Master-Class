####
# indexing basically means that withing the string characters,
# each are a indetified by an integer
#  
# 
# 
# #  

#         01234567890123
# parrot = "Norwegian Blue"

# print (parrot)

# # expected results is to show w
# print (parrot [3])
# print ()
# #Reason being is that when tryi

# # Mini Challenge

# # Add some code to the program, so that it prints out we win.
# # Each character should appear on a separate line.
# # The program should get the characters from the parrot string, using indexing
# # The w is already printed out, you just need to print out the remaining 5 characters.
# # with the text that is already being printeed, the final output from the program should be:
# #Answer:
# # W
# # e
# # 
# # W
# # i
# # n
# print (parrot [3])
# print (parrot [4])
# print (parrot [9])
# print (parrot [3])
# print (parrot [6])
# print (parrot [8])

# print ()

# # negative indexing
# #                       
# #parrot = "Norwegian Blue"
# print (parrot[-11])#W
# print (parrot[-10])#E
# print (parrot[-5])#Space
# print (parrot[-11])#W
# print (parrot[-8])#i
# print (parrot[-6]) #n

# print ()

# print (parrot [3 - 14])
# print (parrot [4 - 14])
# print (parrot [9 - 14])
# print (parrot [3 - 14])
# print (parrot [6 - 14])
# print (parrot [8 - 14])



# Slicing 

# parrot = "Norwegian Blue"

# # we are telling python that we want to start at position 0 and slice up to position 6 nothing more
# print (parrot [0:6]) # Norweg 
# our first slice was [0:6]
# the slice starts at index position 0.
# it exxtends up to (but no including) position 6
# print ()
# print (parrot [3:5]) # we
# # our next slice was [3:5]
# # The slice starts at index position 3
# # IT extends up to (but not including) position 5.
# print ()
# print (parrot [0:9]) # Norwegian
# #Then we had the slice [0:9]
# # This slicestarts at index position 0
# # it extends up to ( but not including) position 9
# print ()
# print (parrot [:9]) # did not provide a start value
# # we can leave off the start value of 0, because the start defaults to the beginning of the sequence.
# # The colon is necessary, otherwise we'd be specifiying the single character at position 9

 
# # Slice the work blue
# print (parrot[10:14])
# print (parrot [10:])

# # first slice is omitted, the slice starts at the beginning of the string
# print (parrot [ :6])
# # second slice is omitted, the slice starts at the end of the string
# print (parrot [6:])

# print (parrot [:6] + parrot [6:])

# print (parrot[:]) #expected output is to print out the whole Norwegian Blue


# letters = "abcdefghijklmnopqrstuvwxyz"
# print (letters [0:4]) #abcd
# print (letters [:4]) #abcd

#Slicing with negative numbers
parrot = "Norwegian Blue"

# we are telling python that we want to start at position 0 and slice up to position 6 nothing more

#The slice starts at index position 0
#It extends up to (but not including) position 6
#We step through the sequence in steps of 2
print (parrot [0:6:2]) #NRE

#The slice starts at index position 0.
#It extends up to (but not including) position 6
#We step through the sequence in steps of 3.
print (parrot[0:6:3]) #NW


number = "9,223;372:036 854,775;807"
seperators = number [1::4]
print (seperators)

values ="".join(char if char not in seperators else " " for char in number).split()
print ([int(val) for val in values])


