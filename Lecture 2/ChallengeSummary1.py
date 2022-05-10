# #Challenge 1

# # Write a program to print a number of options, and all the user to select an  option from the list.
# # The options should be numbered from 1 to 9, although you can use less than nine options if you want to.
# # Make sure that there are at least four options
# # EG: 
# # 1. Learn Python
# # 2. Learn Java
# # 3. Go swimming
# # 4. Have Dinner
# # 5. Go to bed
# # 0. Exit



# #once they hit enter list of options should appear
# print("Please select a number of the listed options below")
# print("1:\tProgrammer")
# print("2:\tTeacher")
# print("3:\tStock Trader")
# print("4:\tStore Clerk")
# print("0:\tExit")

# while True:
#     choice = input()
    
#     if choice == "0":
#         print("you have exited")
#         break
#     elif choice in "1234":
#         print("You chose {}".format(choice))


for value in range (11):
    value = value * 2
    print(value)