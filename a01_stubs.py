######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
birthyr = ((input("What year were you born in? ")))
print(birthyr + "?")

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if birthyr == '2000':
    print("You were born in the year of the Dragon!")
elif birthyr == '2001':
    print("You're a sssssnake!")
elif birthyr == '2002':
    print("You have horsepower in you.")
elif birthyr == '2003':
    print("You're the GOAT!")
elif birthyr == '2004':
    print("You're a silly monkey!")
elif birthyr == '2005':
    print("You're a rooster!")
elif birthyr == '2006':
    print("You're a dawg!")
elif birthyr == '2007':
    print("You're a filthy pig.")
######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
friend = input("What is your friend's birth year?")
print(friend + "?")
if friend == '2000':
    print("They were born in the year of the Dragon!")
elif friend == '2001':
    print("They're a sssssnake!")
elif friend == '2002':
    print("They have horsepower in them.")
elif friend == '2003':
    print("They're the GOAT!")
elif friend == '2004':
    print("They're a silly monkey!")
elif friend == '2005':
    print("They're a rooster!")
elif friend == '2006':
    print("They'ree a dawg!")
elif friend == '2007':
    print("They're a filthy pig.")
# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
