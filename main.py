# Programmers: Antonio Dueno
# Course: CS151, Zelalem Yalew
# Due Date: 11/7/2024
# Programming Assignment: 3
# Problem Statement: Create a program that can create and display different ASCII art and string decorations to the user.
# Data In: User input for if they want to output a circle, a set of lines, or a random design.
# Data Out: Different designs depending on user input
# Credits: Class discussion of functions

import random

# Purpose: Prints circle
# Name: circle
# Parameter: none
# Return: none
def circle():
    print("       * * * * *  \n    *             * \n  *                 * \n *                   *")
    print(" *                   * \n  *                 * \n    *             * \n       * * * * *  ")

# Purpose:
# Name:
# Parameter:
# Return:
def lines():
    count = 0
    number_of_lines = input("How many lines do you want?:")
    while not (number_of_lines.isdigit()):
        number_of_lines = input("Please enter a valid number:")
    else:
        number_of_lines = int(number_of_lines)
    characters = str(input("What do you want your lines to be made of?:"))
    character_repeat = input("How many times do you want the characters to repeat?:")
    while not (character_repeat.isdigit()):
        character_repeat = input("Please enter a valid number:")
    else:
        character_repeat = int(character_repeat)
    while count < number_of_lines:
        print(characters * character_repeat)
        count += 1

# Purpose:
# Name:
# Parameter:
# Return:
def random_design():
    print(" Alien:\n       *    *    \n       |    |     \n     ----------\n    |          |\n   |  **    **  |\n   |  **    **  |\n "
      "  |  **    **  |\n   |     - -    |\n   |            |\n   |  *      *  |\n    |   ****   |\n     ----------")


print("   &&&&&&&&&&&&\n &&&&&&&&&&&&&&&&\n &&&&&&&&&&&&&&&&\n &&&&&&&&&&&&&&&&\n ")