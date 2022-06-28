valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print('Age can not be negative.')
        else:
            valid_input = True
    except ValueError:  # or just  except:
        print("Invalid (not an integer)")
if age % 2:
    print(f"{age} is odd")
    # print("{} is odd".format(age))
else:
    print(f"{age} is even")
    # print("{} is even".format(age))

