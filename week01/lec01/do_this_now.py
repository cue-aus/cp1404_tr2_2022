# get user input
age = int(input('Enter age between 0 and 150: '))
while age < 0 or age > 150:
    print('Invalid age')
    age = int(input('Enter age between 0 and 150: '))
print('Your age:', age)

