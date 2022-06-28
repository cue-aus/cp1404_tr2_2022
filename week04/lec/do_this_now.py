vowel_str = "aieou"
name = input("Enter fullname: ")
while len(name) == 0:
    name = input("Enter fullname: ")
no_of_vowels = 0
for i in range(len(name)):
    if name[i] in vowel_str:
        no_of_vowels += 1
print("Out of {} letters, {} has {} vowels".format(len(name), name, no_of_vowels))
