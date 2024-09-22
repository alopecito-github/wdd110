"""
Author: Tirso Lopez
Activity cse111 week 01 - tyre volume calculator

Assignment: Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

"""
#import math module , i will use the math.py function
import math
from datetime import date

#get user input

today = date.today()
tire_width = float(input("Enter the width of the tire in mm (ex 205):  "))
aspect_radio = float(input("Enter the aspect ratio of the tire (ex 60):   "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15):   "))

#compute the volume by using the formula

volume = (math.pi * (tire_width**2) * aspect_radio * (tire_width * aspect_radio + 2540 * diameter)) / 10000000000
#round the volume to 2 decimals points
volume = round(volume,2)
#print results - claculating th correct volume
print(f"The approximate volume is {volume:.2f} liters ")

# The assigment asked us to choose 3 common tires sizes and look for their prices, I used an If -elif and else statement to display the price of this sizes
if tire_width == 205 and aspect_radio == 60 and diameter == 18:
    print(f"the price of this tire is: $100!")
elif tire_width == 215 and aspect_radio == 50 and diameter == 17:
    print(f"the price of this tire is: $125!")
elif tire_width == 245 and aspect_radio == 50 and diameter == 19:
    print(f"the price of this tire is: $150!")
else:
    print("Unfortunately we don't have those tires in stock!")

# the programs ask if the perosn want's to buy the tires
buying = (input("do you want to buy the tires?[Yes/No] "))
if buying =="Yes":
    phone = input("what is your phone number ?")
else:
    phone = "none"
    print("Thanks anyway")

# Open a text file named cities.txt in append mode.
with open("volumes.txt", "at") as volumes_file:
  # Print a city's name and information to the file.
  print(f"today's date {today},{tire_width}, {aspect_radio},{diameter}, {volume}, {phone}", sep="\n", file=volumes_file, flush=False)



