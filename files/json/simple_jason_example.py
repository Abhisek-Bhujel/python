import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

with open("output.json", 'w') as o:
    json.dump(languages,o)

with open("output.json", 'r') as o:
    data = json.load(o)
    
print(data)
print(data[2])
    