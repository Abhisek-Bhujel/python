print("Today is a good day to learn Python")
print('Python is fun')
print("Pythons's string are easy to use")
print('We can even include "quotes" in strings')

print(r"C:\Users\timbuchalka\notes.txt")
print("C:\\Users\\timbuchalka\\notes.txt")
print()

#Strings are sequence datatypes.

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print()
#Java equivalent is  System.out.println(parrot.charAt(3));

#Mini challenge
#print we win
print(parrot)
print(parrot[3]+'\n'+ parrot[4] +'\n\n' + parrot[3] + '\n' + parrot[6] + '\n' + parrot[8])
print()

#Negative indexing
print(parrot[-1])    #prints e
print(parrot[-14])   #prints N

#Slicing
print(parrot[0:6])   #prints Norweg upto but not including index 6
print(parrot[3:5])   #prints we
print(parrot[0:9])   #prints Norwegian
print(parrot[:9])    #prints Norwegian
print(parrot[10:14]) #prints Blue
print(parrot[10:])   #prints Blue
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] , parrot[6:])
print(parrot[:])

#Negative Slicing

print(parrot[-4:-2]) #prints Bl
print(parrot[-4:12]) #prints Bl

#Step Slicing
# Norwegian Blue
print(parrot[0:6:2]) #prints Nre
print(parrot[0:6:3]) #print Nw

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[-1:-27:-1]
backwards1 = letters[25::-1]
backwards2 = letters[::-1]
print(backwards)
print(backwards1)
print(backwards2)

# Challenge
# produce characters qpo
# produce characters edcba
# produce the last 8 characters in reverse order zyxwvuts

print(letters[-10:-13:-1])
print(letters[-22::-1])
print(letters[:-9:-1])
print()
#get last 4 charcters
print(letters[-4:])       #prints wxyz
#get last character
print(letters[-1:])      #prints z
#get first character
print(letters[:1])         #prints a
