shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print ("buy " + item)


for item in shopping_list:
    if item == "spam":
        # continue keyword is used to end current iteration a for loop (while loop), and continues to the next iteration
        continue
    
    print ("buy " + item)