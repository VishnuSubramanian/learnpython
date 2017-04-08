#creating a list variable to store the list getting from the user
items = []

def welcome_function():
    print('welcome to the loopy function challenge')
    print('I know it is tough but you can crack it')

welcome_function()

def list_adding(new_items):
    items.append(new_items)
    print("The newitem is {}".format(new_items))

def loopy(new_items):
    print('Here is the list of items')
    for new_items in items:
        if new_items[0] =='a':
            continue
            print("Sorry ! We can't accept name with starting letter a")
        else:
            list_adding(new_items)


while True:
    new_items = input("> ")
    loopy(new_items)
