#Print the table of weights to shipping price
print("Here is the table for shipping charges: \n")
print("WEIGHT          | PRICE")
print("------------------------")
print("2 lbs. or less  | $1.50")
print(">2 - 6 lbs.     | $3.00")
print(">6 - 10 lbs.    | $4.00")
print("over 10 lbs.    | $4.75")

#Store the user's package weight in a variable and convert it to a float value
weight = float(input("\nHow heavy is your package?: "))

#If the weight is 2 or less pounds
if weight <= 2:
    print("You will pay $1.50 for shipping.")

#If the weight is 6 or less pounds
elif weight <= 6:
    print("You will pay $3.00 for shipping.")

#If the weight is 10 or less pounds
elif weight <= 10:
    print("You will pay $4.00 for shipping.")

#If the package is more than 10 pounds
else:
    print("You will pay $4.75 for shipping.")
