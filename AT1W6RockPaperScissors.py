# Author: Jason Brown
# Date: 17/05/22
# Version 1.0

# Rock, Paper, Scissors game
# Two players

print("Welcome to Rock, Paper, Scissors!")
print("Lets Begin...")
name1=input("Player 1: What's your name? ")
name2=input("Player 2: What's your name? ")
print()

print("Hello " + name1 + " and " + name2 + "\n")
print(name2 + ": Close your eyes!")

choice1=input(name1 + " enter 'r' for rock, 'p' for paper, and 's' for scissors:")      
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n")
choice2=input(name2 + " enter 'r' for rock, 'p' for paper, and 's' for scissors:")

# Compares Player 1 (name1) choice with Player 2 (name2). 
if (choice1=="r"):
    if (choice2=="r"):
        print("The winner is no one, the game is a draw")
    elif (choice2=="s"):
        print("The winner is ", name1, "as", name1, "chose", choice1,"and", name2, "chose", choice2)
    elif (choice2=="p"):
        print("The winner is ", name2, "as", name2, "chose", choice2,"and", name1, "chose", choice1)
    
elif (choice1=="p"):
    if (choice2=="p"):
        print("The winner is no one, the game is a draw")
    elif (choice2=="r"):
        print("The winner is ", name1, "as", name1, "chose", choice1,"and", name2, "chose", choice2)
    elif (choice2=="s"):
        print("The winner is ", name2, "as", name2, "chose", choice2,"and", name1, "chose", choice1)

elif (choice1=="s"):
    if (choice2=="s"):
        print("The winner is no one, the game is a draw")
    elif (choice2=="p"):
        print("The winner is ", name1, "as", name1, "chose", choice1,"and", name2, "chose", choice2)
    elif (choice2=="r"):
        print("The winner is ", name2, "as", name2, "chose", choice2,"and", name1, "chose", choice1)
      
print("Thanks for playing rock, paper, scissors") 