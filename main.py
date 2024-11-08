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
    print("       * * * * *  \n"
          "    *             * \n"
          "  *                 * \n"
          " *                   *")
    print(" *                   * \n"
          "  *                 * \n"
          "    *             * \n"
          "       * * * * *  ")

# Purpose: Allow user to design specified number of lines
# Name: lines
# Parameter: none
# Return: none
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

# Purpose: Prints random design
# Name: random_design
# Parameter: none
# Return: none
def random_design():
    design_picker = 0
    design_picker = random.randint(1, 3)

    if design_picker == 1:
        print(" Alien:\n "
          "      *    *    \n"
          "       |    |    \n"
          "     ----------\n"
          "    |          |\n"
          "   |  **    **  |\n"
          "   |  **    **  |\n"
          "   |  **    **  |\n "
          "  |     - -    |\n "
          "  |            |\n"
          "   |  *      *  |\n "
          "   |   ****   |\n"
          "     ----------")


    elif design_picker == 2:
        print("Mushroom:\n"
          "  &&&&&&&OOOO&&\n"
          " &&&OOO&&&OO&&&&&\n"
          " &&&OOO&&&&&&&OOO\n"
          " &&&OO&&&&&&&&&OO\n"
          "     (     )\n"
          "      |   |\n"
          "      |   |\n"
          "      |   |\n"
          "      )   ( ")

    elif design_picker == 3:
        print("Cat:\n"
          "     /\\  /\\ \n"
          "    ( ^ * ^ )     /\\      \n"
          "      \\       \\  \\ \\ \n"
          "      /        | / /  \n"
          "      \\  \\ /  /   /  \n ")

def main():
    print("Hello! In this program you will be able to view different kinds of ASCII designs. \n "
          "You can also design your own ASCII design via inputting what characters you wish \n"
          "to be in a series of lines. Please enter 'C' for view a circle, 'L' for line creation, \n"
          "'R' for random design, and 'E' for exiting the program. \n ")
    user_choice = str(input("What will you do?: "))
    while user_choice != 'C' and user_choice != 'L' and user_choice != 'R' and user_choice != 'E':
        user_choice = str(input("Please enter C or L or R or E: "))
    if user_choice == "C":
        circle()
    elif user_choice == "L":
        lines()
    elif user_choice == "R":
        random_design()
    elif user_choice == "E":
        print("Thank you for using this program!")
        exit()



main()