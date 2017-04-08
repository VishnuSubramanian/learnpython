# make a list to hold onto our items
shopping_list = []
# print out instructions on how to use the app
print("What should you pick up in the store")
print("Enter 'DONE' to stop")

while True:

# ask for new items

    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    # add new items to our list

    shopping_list.append(new_item)

# print out the list
print("Here is your list")
for item in shopping_list:
    print(item)
