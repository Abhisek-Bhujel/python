farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals = farm_animals.union(wild_animals)
print(all_animals)

all_animals2 = farm_animals | wild_animals
print(all_animals2)