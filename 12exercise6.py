#Recursion

def main(): #Main function
    factorial = int(input("What number would you like to find the factorial of?: ")) #Get the user's input
    final_number = 1 #Set the final number to 1
    iter = 1 #Set the iteration to 1

    while iter <= factorial: #While the iteration is less than the user's number
        final_number = final_number * iter #Add the product of the final number and iteration ex.) 1 * 2 -> 2 * 3 -> 6 * 4
        iter += 1 #Add one to the iteration

    return final_number #After the loop is finished return the final number

print(main()) #Run the main function and print the result

input("Press enter to terminate. . .")
