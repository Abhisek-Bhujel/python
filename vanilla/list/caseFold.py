pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)   #No sort method for strings only list
print(pangram)
print(letters)
print(sorted(pangram,key=str.casefold))

name = ["Graham",
        "John",
        "terry",
        "mary",
        "Terry"]
name.sort()
print(name)

name.sort(key=str.casefold)
print(name)


