"""
This generates a discount if the subtotal is 
greater than or equal to 50, and if 
it a Tuesday or a Wednesday.
Seth Ricks 
CSE111
"""

from datetime import datetime 
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
#day_of_week = 2

subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    print(f"Discount amount: {(subtotal * 0.1):.2f}")
    subtotal = subtotal * 0.9

sales_tax = (0.06) * subtotal

print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: {total:.2f}")