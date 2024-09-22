"""
Author: Tirso Lopez
Activity cse111 week 01 - Discount calculator

A program must compute and print the number of boxes necessary to hold the items.
"""
import math

# Let's begin by asking for input - Number of items and number of items per pack #


# Import the datetime class from the datetime
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
discount_amount = 0
subtotal = 1
disc_rate = 10
tax_rate = 6

while subtotal > 0: # while loop, it will be break once the input is 0
    subtotal = int(input('What is the subtotal: '))
   
    if day_of_week in (1,2):# conditional if statement, days 1 & 2 are tuesdays and wenesdays
        if subtotal >= 50:
            discount_amount = subtotal * disc_rate/100
            subtotal= subtotal - discount_amount
            tax = subtotal * tax_rate /100
            total = subtotal + tax
            print(f"discount_amount: {discount_amount:.2f}")
            print(f"Sales tax amount: {tax:.2f}")
            print(f"Total: {total:.2f}")
        elif subtotal == 0:
            print("Bye")
            break
        elif subtotal < 49 :
            missing_amount = 50 - subtotal
            print(f"You need to purchase an additional of:  {missing_amount:.2f}")
            tax = subtotal * tax_rate /100
            total = subtotal + tax
            print(f"Sales tax amount: {tax:.2f}")
            print(f"Total: {total:.2f}")       
    else:
        discount_amount = 0
        tax = subtotal * 6 /100
        total = subtotal + tax
        print(f"Sales tax amount: {tax:.2f}")
        print(f"Total: {total:.2f}")



    


#print(f"For {items} items, packing  items in each box, you will need {items_per_pack} boxes.")

print("----------------------------------------")
