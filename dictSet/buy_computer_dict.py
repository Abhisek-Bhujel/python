available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi-cable",
                   "6": "dvd drive"
                   }

choice = '-'
computer_parts = []

while choice != '0':
    choice = input(">")
    if choice in available_parts:
        chosen_part = available_parts[choice]
        print(f"Adding {chosen_part}")
        computer_parts.append(chosen_part)
    else:
        print(f"Choice {choice} is not in the dictionary.\nChoose from following option  or 0 to quit")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
print(computer_parts)