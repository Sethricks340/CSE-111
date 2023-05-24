import csv

def main():

    student_dictionary = read_dictionary("students.csv", 0)

    print()
    I_number = input("Enter I-number: ")

    I_number = I_number.replace("-", "")

    if not I_number.isdigit():
        print("Sorry, not a valid number.")
    elif len(I_number) > 9: 
        print("Too many digits")
    elif len(I_number) < 9:
        print("Too few digits")

    else: 
        if I_number in student_dictionary:
            print(f"{student_dictionary[I_number][1]}")

        else:
            print("No such student.")
    print()


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    students_dictionary = {}

    with open(filename, "rt") as students_file:

        reader = csv.reader(students_file)

        next(reader)

        for line in reader:

            #clean_line = line.strip()
            #clean_line = clean_line.split(",")

            students_dictionary[line[key_column_index]] = line

    return students_dictionary


if __name__ == "__main__":
    main()
