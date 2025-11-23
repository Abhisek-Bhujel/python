for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:<4}".format(i, i**2, i**3))
    
print(f"Pi is approximately {22/7 : 12.50f}")
meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print(meal1)
print(meal2)
print(meal3)
print(meal4)