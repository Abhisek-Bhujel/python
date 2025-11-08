current_choice = "-"
computer_parts = []   #create an empty list

while current_choice != '0':
    print("""Computer parts:
    To add computer press 1
    To add monitor press 2
    To add keyboard press 3
    To add mouse press 4
    To add mouse mat press 5
    To add HDMI press 6
    To exit press 0
             """)
    current_choice = input()
    if current_choice in "123456":
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("HDMI")
        print("Adding: {}".format(current_choice))
    elif current_choice == '0':
        print("Exiting Program")
    else:
        print("Invalid choice")

print("Computer parts:")
print(computer_parts)
            