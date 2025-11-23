from contents_quantities import pantry, recipes
print(pantry)
chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")
beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")
print()
print('Pantry now contains beans')
print(pantry)

