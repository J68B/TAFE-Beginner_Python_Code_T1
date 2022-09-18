# -*- coding: utf-8 -*-
"""
Student: Jason Brown
ID: 469730808
Date: 11th June 2022
Ver: 1.0
PLEASE OPEN IN THONNY FOR SOME REASON SPYDER DOES NOT IMPORT PYFIGLET
"""

# This is a maths quest to help students with thier times tables

# import required modules
print("Welcome to Maths Quest!")


# Get student name and choices
name=input("What is your name: ")
table=int(input(name + ", which times table do you wish to practice? (1-12): "))

# check to ensure table is in range
if table >= 1 and table <= 12:
    print()
    print("Ok " + name + "," + " on a piece of paper, write down the " + str(table) + " times table from 1 to 12. When you're ready I'll show you the answers so you can check your work.")
    
# check if the student wishes to continue with an advanced table    
# else:   
#     choice=input("This is an advanced table, did you still want to continue? y/n: ") 
#     if choice.lower()=='y':
#         print("Ok, proceeding with an advanced table!")
#     elif choice.lower()=='n':
#         print()
#         print("Program terminated")
#         sys.exit()
        
# check if student is ready and print out the chosen times table
ready=''
while ready.lower() !='y':
    ready=(input("Are you ready: "))
    print()
    
for i in range(1, 13):
    print(table, "X", i, "=", table*i)     

print()
answer=input("Did you get them all correct? y/n: ")
if answer.lower() == 'y':
    print()
    print("Great job! Thank you for playing Maths Quest")       
else: 
    print()
    print("Better luck next time, keep practicing!")
    
# Future changes
# create a loop that asks student if they wish to play again before exiting
# install and import pyfiglet
# create advanced table options
# create loops for unexpected key entrys

