import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

def main():
    try:
        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        products_dictionary = read_dictionary("products.csv", 0)

        print()
        print("Mr. Boolean Express") #name of the store

        #Open the file with the buyer's requested items
        with open("request.csv", "rt") as request_file:

            reader = csv.reader(request_file)

            #skip header
            next(reader)
            
            print()
            print("Requested items:")

            total_item_count = 0
            subtotal = 0
            for line in request_file:

                clean_line = line.strip()
                clean_line = clean_line.split(",")

                product_number = clean_line[0]

                #print requested item name, amount requested, price 
                print(f"{products_dictionary[product_number][1]}: {clean_line[1]} @ {products_dictionary[product_number][2]}")

                #partial total item count
                total_item_count += int(clean_line[1])

                #multiply the price of the item by the number of items to find partial subtotal
                subtotal += float(products_dictionary[product_number][2]) * int(clean_line[1])
        
        print()
        print(f"Number of items: {total_item_count}")

        #Discount if it is Tuesday or Wednesday
        if current_date_and_time.weekday() in (1,2):
            subtotal = subtotal * 0.90
            if current_date_and_time.weekday() == 1:
                print("Discount Tuesday! Everything is 10 percent off!")
            elif current_date_and_time.weekday() == 2:
                print("Discount Wednesday! Everything is 10 percent off!")

        #Sales tax is +6%
        tax = subtotal * 0.06
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales tax: {tax:.2f}")
        print(f"Total: {subtotal + tax:.2f}")
        print()
        print(f"Thank you for shopping at Mr. Boolean Express! Come back soon!")

        # Use an f-string to print the current
        # day of the week and the current time.
        # Example: Monday March 06 11:33 AM 2023
        print(f"{current_date_and_time:%A %B %d %I:%M %p %Y}")
        print()

    except FileNotFoundError:
        print("Error: missing file")

    except PermissionError:
        print("Error: you do not have permission to access this file.")

    except KeyError:
        print("Error: unknown product ID in the request.csv file")
        print(f"'{clean_line[0]}'")


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

    products_dictionary = {}

    with open(filename, "rt") as products_file:

        reader = csv.reader(products_file)

        #skip header
        next(reader)

        for line in reader:

            #set item in products_dictionary at the key index equal to the product
            products_dictionary[line[key_column_index]] = line

    return products_dictionary

if __name__ == "__main__":
    main()