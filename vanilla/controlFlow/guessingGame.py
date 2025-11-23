answer = int(input("Type no between 0 - 9: "))
guessedNumber = int(input("Guess no between 0 - 9: "))

if answer == guessedNumber:
    print("You guessed correct. The number was {}". format(answer))
else:
    print("Your guess no {} is incorrect.\nCorrect answer was {}".format(guessedNumber, answer))
    