shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "bacon",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(id(shopping_list))    # 140610540762816
print(id(another_list))     # 140610540762816

shopping_list += ["cookies"]
print(shopping_list)    # ['milk', 'pasta', 'eggs', 'bacon', 'bread', 'rice', 'cookies']
print(id(another_list))     # 140610540762816