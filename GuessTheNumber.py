import random


# this is the Computer turn
print("==========================================================")
print("welcome to guess the number") 
print("computer has chosen a number now its your turn to guess it")
print("==========================================================")

NumComp = random.randint(0,100)





#this is for the user input 
while(True):
    NumGuess = int(input("Enter the number between 0 to 100="))

    if(NumComp==NumGuess):  
        print("Hey You have Guessed it right it is",NumComp) 
        break
    elif(NumGuess < NumComp):
        print("The Number is more than ",NumGuess)
    elif(NumGuess> NumComp):
        print("The Number is less ",NumGuess)