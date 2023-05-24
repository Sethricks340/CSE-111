"""
Calculate the volume of a car tire
and asks for information for purchasing.
-Seth Ricks
CSE 111
"""

import math
from datetime import datetime
current_date_and_time = datetime.now()

def compute_tire_volume(w, a, d):
    """
    Computes the volume of a tire.
    Parameters
        width: the width of the tire
        aspect_ratio: the aspect ratio of the tire
        diameter: diameter of the tire
    Return: the volume of the tire
    """
    volume = (math.pi * (w ** 2) * a * ((w * a) + (2540 * d))) / (10 ** 10)
    return volume

print()
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = compute_tire_volume(w, a, d)
print()
print(f"The approximate volume is {volume:.2f} liters")    

print()

buy = input("Would you like to purchase tires with the dimensions given? (yes/no) ")
if buy.lower() == "yes":

    print("Please enter the following information in order to complete your purchase: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number (xxx-xxx-xxxx): ")
    print("Thank you! Your order has been recorded and should be ready shortly.")

else:
    print("Come back next time!")

with open("volumes.txt", "at") as volumes_file:
    
    if buy.lower() == "yes":
       print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}, {last_name.title()}, {first_name.title()}, {phone_number}", file=volumes_file)  
    
    else:       
       print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}", file=volumes_file)
print()