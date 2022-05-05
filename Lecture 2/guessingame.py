answer = 5 

print ("please guess a number 1 through 10: ")
guess = int(input())

#Challenge
# change the condition "if guess != answer:" to "if guess == answer:"
# then change the program to give the correct results

#answer
if guess == answer:
    print ("You got it the first time")
else:    
    if guess > answer:
        print ("guess lower")
    else: #guess must be greater than answer
        print ("Please guess higher")
    guess = int (input())
    if guess  == answer:
        print ("Well done, you have guess correctly")
    else:
        print ("sorry, you have guessed incorrectly")
# else:
#     print ("You got it the first time")

# if guess < answer:
#     print ("Please guess higher")
#     # single equal sign is when you're assigning a variable
#     guess = int(input())
#     # double equal sign is when you're seeing if they're any sort of equality
#     if guess == answer:
#         print ("well done you've guess correctly")
#     else: 
#         print ("sorry you did not guess correctly")
# elif guess > answer:
#     print ("please guess lower")
#     guess = int(input())
#     if guess == answer:
#             print ("well done, you guessed it")
#     else: 
#         print ("sorry, you have not guess correctly")
# else:
#     print ("You got it the first time")