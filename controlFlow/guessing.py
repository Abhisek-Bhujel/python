import random

def get_integer(prompt):
    """
    Prompt the user to enter an integer and validate the input.

    Repeatedly asks the user for input until a valid integer is entered. 
    If the user enters a non-numeric value, it prints an error message 
    and prompts again.

    Args:
        prompt (`str`): The message displayed to the user when asking for input.

    Returns:
        `int`: The integer value entered by the user.
    """
    while True:
        receivedInt = input(prompt)
        if receivedInt.isnumeric():
            return int(receivedInt)
        print("Invalid input: Please provide input again")
        
        
highest = 10
answer = random.randint(1,highest)
print(answer)
print("Please guess number between 1 and {} or 0 to quit: ".format(highest))


while True:
    guess = get_integer(": ")
    print(guess)
    if guess == 0 or guess == answer:
        if guess == answer:
            print("You guessed it correct")
        else:
            print("You Quit. Try again next time")
        break
    else:
        print("Your guess is incorrect. Try again")
    