answer = 5
guess = int(input("Please guess number between 1 and 10: "))

if guess < answer:
    guess = int(input("Please guess higher: "))
    if guess == answer:
        print("Well done, you guessed it.")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    guess = int(input("Please guess lower: "))
    if guess == answer:
        print("Well done, you guessed it..")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time.")
