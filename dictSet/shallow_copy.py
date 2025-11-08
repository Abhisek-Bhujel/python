import copy
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly"
}

# things = animals.copy()
things = copy.deepcopy(animals)
animals["teddy"] = "toy"
print(things["teddy"])