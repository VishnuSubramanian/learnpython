#have a help command
#have a show command
#clean the code

# make a list to hold onto our items
shopping_list = []

# print out instructions on how to use the app

## adding functions for easy and cleaning the code\

def help_command():
    print("What should you pick up in the store")
    print("""Enter 'DONE' to stop
Enter 'HELP' to open help options
Enter 'SHOW' to show results""")

help_command()

def show_list():
    print("Here is your list")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("New Items is {} and now the list has {} items".format(new_item,len(shopping_list)))

while True:

# ask for new items

    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        # add new items to our list
        break
    elif new_item == 'HELP':
        help_command()
        continue

    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

    # shopping_list.append(new_item)

# print out the list
show_list()
