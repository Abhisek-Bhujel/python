# for t in enumerate("abcdefgh"):
#     print(t)

# table = ("Coffee table", 200, 100, 75, 34.50)
# name, length, width, height, price = table
# print(length * width)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

print(len(albums))
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))