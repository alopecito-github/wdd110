"""
Author: Tirso Lopez
Activity cse111 week 01 - Boxes

A program must compute and print the number of boxes necessary to hold the items.
"""
import math

# Let's begin by asking for input - Number of items and number of items per pack #
items = int(input('Enter the number of items: '))
number_per_pack = int(input('Enter the number of items per box: '))

items_per_pack =  math.ceil(items /number_per_pack)

print(f"For {items} items, packing {number_per_pack} items in each box, you will need {items_per_pack} boxes.")

print("----------------------------------------")