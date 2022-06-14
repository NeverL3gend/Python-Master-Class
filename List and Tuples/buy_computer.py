from logging.config import valid_ident


available_parts = ["computer",
                   "monitor", 
                   "keyboard", 
                   "mouse",  
                   "HDMI",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
valid_choices = []
for i in range (1, len(available_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        print("adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else: 
        print("Please add options from the list below: ")
        for number, parts in enumerate (available_parts):
            print("{0}: {1}".format(number + 1, parts))
        
    current_choice = input()
print(computer_parts)