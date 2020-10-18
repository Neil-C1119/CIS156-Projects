#Start of try
try:
    #This opens the file as the var numbers, then closes the file once finished running
    with open("numbers.txt", "r") as numbers:
        #Variable for each line of the file
        lines = numbers.readlines()
        #Variable for the amount of lines in the file
        line_amount = len(lines)
        #Variables for calculation and the final answer
        calculate = 0
        iter = 0
        final_number = 0

        #If there are multiple lines
        if line_amount > 1:
            #For each line
            for line in lines:
                #The string is stripped of the newline character and converted into a floating point
                number = float(line.strip("\n"))
                #Add the number to the calculate variable
                calculate = calculate + number
                #Record the amount of iterations AKA how many numbers there are
                iter = iter + 1
            #Calculate the final number
            final_number = calculate / iter
            #Print the final number rounded to 2 decimal places
            print("The average is", round(final_number, 2))

        #If there is only one line
        elif line_amount == 1:
            #Reset to the beginning of the file since we already read it for the lines variable above
            numbers.seek(0)
            #Variable to hold the string on the only line
            line = numbers.readline()
            #Variable that holds a list of each number that is separated by spaces
            numbers = line.split()
            #For each number in the numbers list
            for number in numbers:
                #Add the number (converted to floating point) to the calculate variable
                calculate = calculate + float(number)
                #Record the amount of iterations AKA how many numbers there are
                iter = iter + 1
            #Calculate the final number
            final_number = calculate / iter
            #Print the final number rounded to 2 decimal places
            print("The average is", round(final_number, 2))

#If there is an IOError during the try statement tell the user the file couldn't be found
except IOError:
    print("File could not be found. . .")

#If there is a ValueError during the try statement tell the user one or more of the values are not valid numbers
except ValueError:
    print("One or more of the values are not valid numbers. . .")
