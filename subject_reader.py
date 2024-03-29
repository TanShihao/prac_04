"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = []
    get_data(data)
    print(data)
    show_data(data)


def get_data(data):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, 'r')
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data


def show_data(data):
    for i in range(len(data)):
        print("{} is taught by {} and has {} student".format(data[i][0], data[i][1], data[i][2]))


main()
