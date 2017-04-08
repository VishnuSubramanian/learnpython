try:
    count = int(input("Hello give me a number: "))
except NameError:
    print("Hi this is no a number you need to give a valid integer")
else:
    print("Hi you selected the number {}".format(count))


def add (arg1,arg2):
    try:
        a = float(arg1)
        b = float(arg2)
    except ValueError:
        return None
    else:
        return true


# items = [1,2,3,4]
def loopy(items):
    for item in items:
        if item == "STOP":
            break
        else:
            print(item)
