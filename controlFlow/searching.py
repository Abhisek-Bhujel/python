shopping_list = ["milk", "pasta","eggs", "spam", "bread", "rice"]

item_To_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_To_find:
#         found_at = index
#         break

if item_To_find in shopping_list:
    found_at = shopping_list.index(item_To_find)

if found_at is not None:    
    print('Item was found at index {}'.format(found_at))
else:
    print("{} not found".format(item_To_find))