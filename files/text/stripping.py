filename = 'Jabberwocky.txt'

with open(filename,'r') as jabber:
    first = jabber.readline()
print(first.strip("'").strip()[::-1])

print("*" * 80) 
print(first)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)


toves_removed = first.removesuffix("toves\n")
print(toves_removed)

print(first[:-3])