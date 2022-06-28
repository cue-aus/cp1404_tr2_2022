"""
Testing for functions
"""


def is_leap(year):
    """return true if year is an Olympic year"""
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


def main():
    print("Start the main function")
    for year in range(1900, 2022):
        if is_leap(year):
            print(year, end=' ')
    print()


if __name__ == '__main__':
    main()

