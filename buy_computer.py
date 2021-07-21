current_choice = "-"
computer_parts = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Pad", "HDMI Cable"]
shopping_list = []  # create an empty list

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {} to your cart".format(computer_parts[int(current_choice)-1]))
        shopping_list.append(computer_parts[int(current_choice)-1])
    else:
        print("Please add options from the list below")
        print("1. Computer")
        print("2. Monitor")
        print("3. Keyboard")
        print("4. Mouse")
        print("5. Mouse Pad")
        print("6. HDMI Cable")
        print("0. to finish")

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