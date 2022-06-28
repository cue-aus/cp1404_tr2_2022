# import math
from math import *

# get user input
age = int(input('Enter age between 0 and 150: '))
while age < 0 or age > 150:
    print('Invalid age')
    age = int(input('Enter age between 0 and 150: '))

if age >= 18:
    print('You are an adult')
else:
    print('You are a child')

print(len('12345678'))

print('abc'.capitalize())

print(2**5)

print(sqrt(4))
