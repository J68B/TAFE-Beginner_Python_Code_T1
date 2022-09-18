# -*- coding: utf-8 -*-
"""
Student: Jason Brown
ID: 469730808
Date: 13th June 2022
Purpose: This is a maths quest game to help students with thier times tables
Ver: 2.0
- changes for version 2.0
    added in pyfiglet banner
    added in option for advanced table
    added in replay option
    fixed some unexpected key entries
"""
# import modules, if pyfiglet is not installed/working with your IDE please comment out lines 16,17,18
import sys
import pyfiglet
mq_banner=pyfiglet.figlet_format("< MATHS QUEST 2.0 >", width=100)
print(mq_banner)

bye=("Thanks for playing MQ 2.0!")
print("Welcome to Maths Quest 2.0!")

# collect student details and table choices
name=input("What is your name: ")
print("Hi " + name + "!!!" + " hope you are ready for a fun challenge!")
while(True):
    try:
        # check if table is basic or advanced
        print()
        table=int(input("Please choose the times table you wish to practice \nfrom (-12) to 12 for basic tables or any other number for advanced!: "))
                
        if table >= -12 and table <= 12:
            print()
            print("Ok " + name + "," + " on a piece of paper, write down the " + str(table) + " times table from 1 to 12.")   
        # check if the student wishes to continue with an advanced table    
        else:
            print()
            choice=''
            while choice.lower() != 'y' or choice.lower() != 'n':
                choice=(input("This is an advanced table, did you still want to play? y/n: ")) 
                if choice.lower()=='y':
                    print()
                    print("You like a challenge I see! proceeding with the " + str(table) + " times advanced table!")
                    break
                elif choice.lower()=='n':
                    print()
                    print(bye)
                    sys.exit()
                    
        # check if student is ready and print out the chosen times table
        ready=''
        print()
        while ready.lower() !='y':
            ready=(input("Press y when ready to see the answers or n to exit the game: "))
            if ready.lower() == 'y':
                break
            elif ready.lower() == 'n':
                print(bye)
                sys.exit()
        print()
        print("See below answers \n")
            
        for i in range(1, 13):
            print(table, "X", i, "=", table*i)     

        # check to see if student got them all correct
        answer=''
        print()
        while answer.lower() != 'y' or answer.lower() != 'n':
            answer=(input("Did you get them all correct? y/n: "))
            if answer.lower() == "y":
                print()
                print("Great job!")
                break
            elif answer.lower() == "n":
                print("Better luck next time, keep practicing!")
                break
        
        print()
        exit=input("Press any key to play again or press n to exit the game: ")
        if exit.lower() !='n': 
          print("Awesome!!!!, lets play again")
        else:    
          print(bye)
          sys.exit()
    
    except ValueError:
            print()
            print(" ** HMMM, THIS GAME ONLY ACCEPTS NUMERIC VALUES FOR TIMES TABLES ** \n ")


# Future changes
# 1. create an option that allows the student to enter the answers within the program instead of using pen/paper
# 2. option if student does not want to do advanced table but wants to stay in game (potential code)
#         close=''
#         while close != 1 or close != 0:
#             close=int(input("If you really want to quit, press 1, or press 0 to enter another times table: "))
#             if close == 0:
#                 print()
#                 break
#             elif close == 1:
#                 print(bye)
#                 sys.exit()
# add some more graphics and colour options