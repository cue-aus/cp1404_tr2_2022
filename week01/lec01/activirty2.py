def main():
    try:
        infile = open("cp1111.csv", 'r')
        for line in infile:
            print(line.strip())
        infile.close()
    except IOError as err:
        print("I/O error: {}".format(err))
# Start the program
main()
