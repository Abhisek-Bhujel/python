name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
print(name, "is", age, "years old")

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of a Jedi")
else:
    print("{} is old enough to vote.".format(name))
