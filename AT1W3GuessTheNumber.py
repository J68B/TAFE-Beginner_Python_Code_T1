## Aurthor: Jason Brown
# Date: 04/05/2022
# Version 1.0
#
#Guess the random number game
#One player vs. the computer

import random
minGuess = 1
maxGuess = 6


#Ask the user for their name and their guess
name = input("What is your name? ")
print()
print("Hi " + name + "!")
print()
print("Think of a number between 1 and 6 inclusive.")
guess = int(input("What is your guess? "))

#Generate a random number and tell the user if they won or lost
secretNumber = random.randint(minGuess, maxGuess)
if (guess == secretNumber):
    print()
    print("Congratulations, you got it right!, the secret number was", (str)(secretNumber))
else:
    print()
    print("You lose - the secret number was", (str)(secretNumber))  
print()
print()
print()
print("Thank you for playing Guess the Number.")

# Hi Friend
# I made changes to your code, you can tell which lines they are as I used multiple comment markers at the start of the line "#####"
# The new code is after this symbol "--->"
# If you have any questions, please let me know

##### Your original code below #####

# import random
# minGuess = 1
# maxGuess = 6

# Ask the user for their name and their guess
# name = input("What is your name? ")
##### print("Hi + name!") ---> print("Hi " + name + "!")
##### print("Enter a number between: ") + minGuess + " and " + maxGuess)) ---> print("Think of a number between 1 and 6 incusive")
# guess = int(input("What is your guess? "))

# #Generate a random number and tell the user if they won or lost
# secretNumber = random.randint(minGuess, maxGuess)
##### if (guess != ?????) ---> if (guess == secretNumber):
#     print("Congratulations, you got it right!") --->  print("Congratulations, you got it right!, the secret number was", (str)(secretNumber))
# else:
#     print("You lose - the number was ???")
    
# print("Thank you for playing Guess the Number.")
 