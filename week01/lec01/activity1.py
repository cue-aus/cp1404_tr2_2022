my_string = 'Hello World'
my_string_1 = my_string
my_string_2 = 'Hello World'

print(my_string == my_string_2)
print(my_string is my_string_2)
text = 'Python Rules!'
# print(text.upper())
text = text.upper()
print(text)

phone = '07 33724157'

print(phone.startswith('07'))

for i in range(0, 15, 3):
    if i < 10:
        print('0' + str(i))
    else:
        print(i)

my_num = 2.265
print('My number is {:6}'.format(my_num))
print('My number is {:5}'.format(my_num))
print('My number is {:4}'.format(my_num))
print('My number is {:4.2f}'.format(my_num))

pieces = 'Cue, Nguyen, jc123456'.split(', ')
print(pieces)
