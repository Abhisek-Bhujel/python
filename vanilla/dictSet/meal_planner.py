from contents_quantities import pantry, recipes

# print(recipes)
# print(pantry)
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

# example = {}
# example["a"] = 9
# example['b'] = 'ram'
# example["a"] = 98

# print(example)

display_dict = {}
shopping_list = {}


def add_shopping_item(data: dict, item: str, quantity: int) -> None:
    """Adding items to shopping list
    """
    # if item in data:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity
    data[item] = data.setdefault(item, 0) + quantity


for index, key in enumerate(recipes):
    # print(f"{index}: {key}")
    display_dict[str(index + 1)] = key


while True:
    print("Please select the item to prepare or 0 to exit")
    for key, value in display_dict.items():
        print(f"{key}: {value}")
    choice = input(">")
    if choice == "0":
        print("You exited the meal planner")
        break

    dish = display_dict[choice]
    ingredients = recipes[dish]
    print(f"The dish you have chosen to prepare is {dish}")
    print("The ingredients required are")
    print(ingredients)

    for item, quantity in ingredients.items():
        if item not in pantry:
            print("Item not in pantry")
            add_shopping_item(shopping_list, item, quantity)
        else:
            if quantity <= pantry[item]:
                print(f"Enough {item}")
            else:
                print(f"You need {(quantity - pantry[item])} of this {item}")
                add_shopping_item(shopping_list, item, quantity)
    
for key, value in shopping_list.items():
        print(f"{key}: {value}")
