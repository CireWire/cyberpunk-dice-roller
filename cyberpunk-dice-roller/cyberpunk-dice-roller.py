#!/usr/bin/python

__author__ = "(CireWire) Eric Gutierrez Jr."
__copyright__ = "Copyright 2022, Dreaded Sushi Studios"
__license__ = "MIT"
__version__ = "1.0.0"

__email__ = "dreaded.sushi@gmail.com"
__status__ = "Complete"

"""

 ______   _______ ___     ___       __   __ _______ __   __ ______     _______ __   __ _______ _______    _______ __   __ _______ _______ __   __ _______ _______ _______ __  
|    _ | |       |   |   |   |     |  | |  |       |  | |  |    _ |   |       |  | |  |       |       |   |       |  | |  |       |       |  |_|  |  _    |   _   |       |  | 
|   | || |   _   |   |   |   |     |  |_|  |   _   |  | |  |   | ||   |  _____|  |_|  |   _   |_     _|   |       |  |_|  |   _   |   _   |       | |_|   |  |_|  |  _____|  | 
|   |_||_|  | |  |   |   |   |     |       |  | |  |  |_|  |   |_||_  | |_____|       |  | |  | |   |     |       |       |  | |  |  | |  |       |       |       | |_____|  | 
|    __  |  |_|  |   |___|   |___  |_     _|  |_|  |       |    __  | |_____  |       |  |_|  | |   |___  |      _|       |  |_|  |  |_|  |       |  _   ||       |_____  |__| 
|   |  | |       |       |       |   |   | |       |       |   |  | |  _____| |   _   |       | |   |_  | |     |_|   _   |       |       | ||_|| | |_|   |   _   |_____| |__  
|___|  |_|_______|_______|_______|   |___| |_______|_______|___|  |_| |_______|__| |__|_______| |___| |_| |_______|__| |__|_______|_______|_|   |_|_______|__| |__|_______|__| 

"""

# Import random module
import random as r

def roll_dice():
  """ Function to roll dice then add the result along with Role level and modifiers"""
    dice = r.randint(1, 10)
    mod = int(input("What is the modifier from skills, cyberware and/or items? "))
    result = dice + mod
    # Ask user if this is a Role check
    role = input("Is this a Role check? (y/n) ")
    if role == "y" or role == "Y":
    # Ask user for Role level and add role level to result
        role_level = int(input("What is the Role level? "))
        result = result + role_level
    elif role == "n" or role == "N":
        pass
    else:
        print("Invalid input. Please try again.")
    # If dice roll is 10, roll again and add to result
    if dice == 10:
        dice = r.randint(1, 10)
        result += dice
    # If dice roll is 1, roll again and subtract from result
    elif dice == 1:
        dice = r.randint(1, 10)
        result -= dice

    return result


# Ask user for diffculty value
difficulty = int(input("What is the difficulty value or DV? "))


def compare_result():
""" Function will compare roll result with the DV """
    result = roll_dice()
    if result >= difficulty:
        print("Success Choomba! Result: " + str(result))
    else:
        print("Failure! Result: " + str(result))

# Call compare_result function
compare_result()

# Ask user if they want to roll again then loop back to difficulty input
while True:
    again = input("Roll again? (y/n) ")
    if again == "y" or again == "Y":
        difficulty = int(input("What is the difficulty value or DV? "))
        compare_result()
    elif again == "n" or again == "N":
        break
    else:
        print("Invalid input. Please try again.")
