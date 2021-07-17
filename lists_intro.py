computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"]

for part in computer_parts:
    print(part)

print()

print(computer_parts[2])

# indexing and slicing works the same with a list as it does with a string
# both strings and lists are sequence types
print(computer_parts[0:3])
print(computer_parts[-1])

# difference between strings and lists is that strings are IMMUTABLE
# which means they cannot be changed

# lists are mutable and you CAN change the contents of a list
