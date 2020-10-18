#Random number game

#Import the random module
import random

#Set the winning number to a random integer between 1 and 100
winning_number = random.randint(1, 100)

#Set play to equal y
play = "y"

#Set the tries to start at 1
tries = 1

#While play doesn't equal n
while play != "n":
    #Set the guess variable to the user's number
    guess = input("\nGuess a number between 1 and 100, or type 'n' to quit: ")
    #If they type n
    if guess == "n":
        #Quit the game
        break
    #If they don't type n
    else:
        #Compare the user's guess to the random number
        if int(guess) > winning_number:
            print("\nToo high! Try again.")
            #Add a try to the counter
            tries = tries + 1
        elif int(guess) < winning_number:
            print("\nToo low! Try again.")
            #Add a try to the counter
            tries = tries + 1
        #If the user guesses the right number
        elif int(guess) == winning_number:
            print("\nYou got it! It took", tries, "tries.")
            #Reset the random number
            winning_number = random.randint(1, 100)
#Thank the player and wait for them to press enter before terminating
input("\n\nThanks for playing! Press enter to exit. . .")
