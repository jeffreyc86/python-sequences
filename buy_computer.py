current_choice = "-"
computer_parts = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Pad", "HDMI Cable"]
# valid_choices = [str(i) for i in range(1, len(computer_parts) + 1)]
valid_choices = []
for i in range(1, len(computer_parts)+1):
    valid_choices.append(str(i))

shopping_list = []  # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {} to your cart".format(computer_parts[int(current_choice)-1]))
        shopping_list.append(computer_parts[int(current_choice)-1])
    else:
        print("Please add options from the list below")
        # for i in range(len(computer_parts)):
        #     print("{}. {}".format(i+1, computer_parts[i]))
        for number, part in enumerate(computer_parts):
            print("{}. {}".format(number + 1, part))
        print("0. to checkout")

    current_choice = input()

if (len(shopping_list) == 0):
    print("You have no items in your shopping cart. Please come again.")
else:
    shopping_list_str = ""
    for i in range(len(shopping_list)):
        if len(shopping_list) == 1:
            shopping_list_str += shopping_list[i]
        else:
            if i == (len(shopping_list) - 1):
                shopping_list_str += "and {}".format(shopping_list[i])
            else:
                if len(shopping_list) == 2:
                    shopping_list_str += "{} ".format(shopping_list[i])
                else:
                    shopping_list_str += "{}, ".format(shopping_list[i])

    print("Your shopping cart includes {}. Thank you for shopping with us!".format(shopping_list_str))