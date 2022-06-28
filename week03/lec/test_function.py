"""
Testing for functions
"""
from math import *
import string

# Initialize the constants
COUNTRIES = ['Australia', 'China', 'India', 'Singapore']


def main():
    print("Start the main function")
    print(f'Square root of 5 is {sqrt(5):.2f}')
    # print("Square root of 5 is {:.2f}".format(sqrt(5)))
    print(celsius_to_fahrenheit(30))
    display_menu()
    option = int(input("Enter 1-4 for a country. Enter 5 to quit: "))
    while option != 5:
        if 0 < option < 5:
            print(COUNTRIES[option - 1])
        else:
            print("Invalid choice")
        display_menu()
        option = int(input("Enter 1-4 for a country. Enter 5 to quit: "))
    print("Bye.")


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0


def count_letters(text):
    """Count the number of letters in text."""
    count = 0
    for character in text:
        if character.lower() in string.ascii_letters:
            count += 1
    return count


def display_menu():
    """Display a list of countries to choose"""
    # no_of_countries = len(COUNTRIES)
    print("\nCountries")
    print("=========")
    for i in range(len(COUNTRIES)):
        print(str(i + 1) + ". " + COUNTRIES[i])


# Start the program
main()
