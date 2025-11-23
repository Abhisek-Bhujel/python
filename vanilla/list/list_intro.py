computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

i= 1
for part in computer_parts:
    print("{}. {}".format(i, part))
    i = i+1
    
print("*" * 50)
print(computer_parts[2])
print(computer_parts[0:3])
print(computer_parts[::-1])

print("*" * 50)

even = [2, 4, 6, 8]
odd =  [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print("*" * 50)

print(len(even))
print(len(odd))

print("*" * 50)
print("mississippi".count("s"))
print("mississippi".count("ss"))
