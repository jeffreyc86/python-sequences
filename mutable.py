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
<<<<<<< HEAD
print(another_list)    # ['milk', 'pasta', 'eggs', 'bacon', 'bread', 'rice', 'cookies']
print(id(another_list))     # 140610540762816

a = b = c = d = e = f = another_list

print(a)    # ['milk', 'pasta', 'eggs', 'bacon', 'bread', 'rice', 'cookies']
print("Adding cream")
b.append("cream")
print(c)    # ['milk', 'pasta', 'eggs', 'bacon', 'bread', 'rice', 'cookies', 'cream']
print(f)    # ['milk', 'pasta', 'eggs', 'bacon', 'bread', 'rice', 'cookies', 'cream']
print(shopping_list)    # ['milk', 'pasta', 'eggs', 'bacon', 'bread', 'rice', 'cookies', 'cream']

=======
print(id(another_list))     # 140610540762816
>>>>>>> 92bd27dc76033166094381e4bcad8c46396fe257
