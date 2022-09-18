"""
Student Name: Jason Brown
Student ID: 469730808
Date:
"""

''' Program design
Prompt the user for a number of rows in the range 1 to 10, with 0 stopping the program
Stop the program if the number of rows is 0
Print an error message and loop back if the number of rows is out of range
Prompt the user for a number of columns in the range 1 to 10
Print an error message and loop back if the number of columns is out of range
Draw a filled rectangle of asterisks (‘*’) with the given number of rows and columns.
Print a blank line and loop back to get new and row and column values '''

#import modules
import sys

print("Welcome to rows and columns, where stars align")

# Prompt the user for a number of rows in the range 1 to 10, with 0 stopping the program
while(True):
    rows=int(input("Please enter the amount of rows from 1-10, or choose 0 to exit: "))
    if rows in range(1,11):
        print("You have chosen wisely and selected", rows, "rows")
        break
    # Stop the program if the number of rows is 0
    elif rows ==0:
        print("Why are you wasting my time choosing 0!, exiting")
        sys.exit()
    # Print an error message and loop back if the number of rows is out of range
    else:
        print("incorrect entry, try again: ") 
        
# Prompt the user for a number of columns in the range 1 to 10        
while(True):
    cols=int(input("Please enter the amount of columns from 1-10: "))
    if cols in range(1,11):
        print("Again, you have chosen wisely and selected", cols, "cols")
        break
    # Print an error message and loop back if the number of cols is out of range
    else:
        print("Enter from 1-10 only please: ")    
        
# Draw a filled rectangle of asterisks (‘*’) with the given number of rows and columns.
print()
for i in range(rows):
    print("*" * cols)

# Print a blank line and loop back to get new and row and column values
print()

