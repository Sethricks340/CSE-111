def main():

    provinces_list = read_provinces("provinces.txt") 

    provinces_list.pop(0)
    provinces_list.pop()

    print(provinces_list)

    count = provinces_list.count("Alberta")


    print()
    print(f"Alberta occurs {count} times.")


def read_provinces(file_name):

    provinces_list = []

    with open(file_name, "rt") as provinces_file:


        for line in provinces_file:

            clean_line = line.strip()

            if clean_line == "AB":

                clean_line = "Alberta"

            provinces_list.append(clean_line)

    return provinces_list



if __name__ == "__main__":
    main()