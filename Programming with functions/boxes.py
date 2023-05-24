"""
Practicing built-in functions in Python
-Seth Ricks
CSE 111
"""
import math

print()
number_of_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
number_of_boxes = math.ceil(number_of_items / items_per_box)

print()
print(f"For {number_of_items} items, packing {items_per_box} items in each box, you will need {number_of_boxes} boxes.")
print()