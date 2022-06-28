"""
Simple Travel Tracker
Name: Cue Nguyen
Date started: 05/10/2021
GitHub URL: https://github.com/JCUB-CP1404/assignment-1-kevin-aus
"""

# import modules
from operator import itemgetter

# Constants
FILE_NAME = "places.csv"
MENU = """Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""

CITY = 0
COUNTRY = 1
PRIORITY = 2
VISITED_STATUS = 3


def load_places(csv_file, list_of_places):
    try:
        infile = open(csv_file, 'r')
        for line in infile:
            temp_list = line.strip().split(',')
            # convert priority from str to int
            temp_list[PRIORITY] = int(temp_list[PRIORITY])
            list_of_places.append(temp_list)
        infile.close()
        print("{} places loaded from {}".format(len(list_of_places), FILE_NAME))
    except IOError as error:
        print("I/O error: {}".format(error))
    # print(list_of_places)


def list_places(list_of_places: list):

    list_of_places.sort(key=itemgetter(VISITED_STATUS, PRIORITY, COUNTRY, CITY))
    num_of_unvisited_places = 0
    num_of_places = len(list_of_places)
    for i in range(num_of_places):
        unvisited_marker = ' '
        if list_of_places[i][VISITED_STATUS] == 'n':
            unvisited_marker = '*'
            num_of_unvisited_places += 1
        print('{}{}.{:10s} in {:15s} priority {:>3d}'.format(
            unvisited_marker,
            # ' ' if list_of_places[i][3] == 'v' else '*',
            i + 1,
            list_of_places[i][CITY],
            list_of_places[i][COUNTRY],
            list_of_places[i][PRIORITY]))
    if num_of_unvisited_places > 0:
        print('{} places. You still want to visit {} places.'
              .format(num_of_places, num_of_unvisited_places))
    else:
        print('{} places. No places left to visit. Why not add a new place?'
              .format(num_of_places))
    # print(list_of_places)


def input_non_empty_string(prompt):
    input_str = input(prompt).strip()
    while len(input_str) == 0:
        print('Input can not be blank')
        input_str = input(prompt).strip()
    return input_str


def input_positive_int(prompt):
    valid_input = False
    input_num = -1
    while not valid_input:
        try:
            input_num = int(input(prompt))
            if input_num > 0:
                valid_input = True
            else:
                print("Number must be > 0")
        except ValueError:  # or just  except:
            print("Invalid input; enter a valid number")
    return input_num


def add_new_place(list_of_places):
    name = input_non_empty_string('Name: ')
    country = input_non_empty_string('Country: ')
    priority = input_positive_int('Priority: ')
    print('{} in {} (priority {}) added to Travel Tracker'.format(
        name, country, priority))
    list_of_places.append([name, country, priority, 'n'])
    # print(list_of_places)


def num_of_visited_places(list_of_places):
    num_of_places_visited = 0
    for i in range(len(list_of_places)):
        if list_of_places[i][3] == 'v':
            num_of_places_visited += 1
    return num_of_places_visited


def mark_a_place_visited(list_of_places):
    is_valid_num = False
    num_of_places = len(list_of_places)
    while not is_valid_num:
        list_places(list_of_places)
        # is there a place to visit?
        if num_of_visited_places(list_of_places) < num_of_places:
            place_num = input_positive_int('Enter the number of a place to mark as visited: ')
            if place_num > num_of_places:
                print('Invalid number. It must be less than or equal to {}'.format(num_of_places))
            elif list_of_places[place_num - 1][VISITED_STATUS] == 'v':
                print('That place is already visited')
            else:
                is_valid_num = True
                list_of_places[place_num - 1][VISITED_STATUS] = 'v'
                print('{} in {} visited!'.
                      format(list_of_places[place_num - 1][CITY], list_of_places[place_num - 1][COUNTRY]))
        else:  # all places are already visited
            is_valid_num = True


def save_places(csv_file, list_of_places):
    try:
        outfile = open(csv_file, 'w')
        for place in list_of_places:
            place_str = place[CITY] + ',' + place[COUNTRY] \
                        + ',' + str(place[PRIORITY]) + ',' + place[VISITED_STATUS]
            print(place_str, file=outfile)
        print('{} places saved to {}'.format(len(list_of_places), csv_file))
        outfile.close()
    except IOError as err:
        print("I/O error: {0}".format(err))


def main():
    print("Travel Tracker 1.0 - by Cue Nguyen")
    list_of_places = []
    load_places(FILE_NAME, list_of_places)
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != 'Q':
        if choice == 'L':
            list_places(list_of_places)
        elif choice == 'A':
            add_new_place(list_of_places)
        elif choice == 'M':
            mark_a_place_visited(list_of_places)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    save_places(FILE_NAME, list_of_places)
    print("Bye.")


if __name__ == '__main__':
    main()
