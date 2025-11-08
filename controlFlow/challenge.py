name = input("What is your name? ")
age = int(input("What is your age?  "))

if 18 <= age <= 30:
    print("Mr.{} Welcome to the party".format(name))
else:
    print("Sorry Mr.{} You cannot come to the party".format(name))
