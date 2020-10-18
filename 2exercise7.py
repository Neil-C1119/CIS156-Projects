#Get the user's input on how many miles they drove and store it in a variable
miles_driven = input("How many miles did you drive?: ")

#Get the user's input on how many gallons they used to drive x miles
gallons_used = input("\nHow many gallons did your " + miles_driven + " mile trip use?: ")

#Calculate the miles per gallon in terms of the user's answers
mpg = round(int(miles_driven) / int(gallons_used), 2)

#Show the user how many miles per gallon their car got that trip
print("Your car's MPG is " + str(mpg) + " miles per gallon!")
