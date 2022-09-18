# -*- coding: utf-8 -*-
"""
Student: Jason Brown
ID: 469730808
Date: 11th June 2022
Ver: 1.0
"""

# This is a maths quest to help students with thier times tables
import sys
print("Welcome to Maths Quest!")


# Get student name and table choice
name=input("What is your name: ")
table=int(input(name + ", which times table do you wish to practice? (1-12): "))

# check to ensure table is in range
if table >= 1 and table <= 12:
    print()
    print("Ok " + name + "," + " on a piece of paper, write down the " + str(table) + " times table from 1 to 12. When you're ready I'll show you the answers so you can check your work.")
else:
    print("Out of range, exiting")
    sys.exit()

# check if student is ready and print out the chosen times table
ready=''
while ready.lower() !='y':
    ready=(input("Are you ready?: "))
    print()
    
for i in range(1, 13):
    print(table, "X", i, "=", table*i)     

# check if student ready to see answers
print()
answer=input("Did you get them all correct? y/n: ")
if answer.lower() == 'y':
    print()
    print("Great job! Thank you for playing Maths Quest")       
else: 
    print()
    print("Better luck next time, keep practicing!")
    
# Future changes
# create advanced table options
# create a loop that asks student if they wish to play again before exiting
# install and import pyfiglet for banner
# create loops for unexpected key entrys

