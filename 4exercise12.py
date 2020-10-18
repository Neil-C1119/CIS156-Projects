#Factorial

#Ask the user to input a number to calculate
number = int(input("Which number would you like to find the factorial of? "))

#Defining the factorial function
def factorialFunc(number):

    #Set the final_number variable to start at 1
    final_number = 1

    #For every number between 1 and the user's number, including the user's number...
    for each in range(1,number + 1):

        #Add final_number * each number to the final number
        final_number = final_number * each

    print("The factorial of", number, "is", final_number)

factorialFunc(number)
