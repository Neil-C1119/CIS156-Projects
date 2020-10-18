#Print the table of quantities and discount percentages
print("Here is the table of discounts: \n")
print(" QUANTITY    | DISCOUNT")
print("------------------------")
print(" 10-19       | 10%")
print(" 20-49       | 20%")
print(" 50-99       | 30%")
print(" 100 or more | 40%")

#Store the user's package amount in a variable and convert it to an integer
package_amount = int(input("\n\nHow many packages will you purchase?: "))

#If the package amount is 10 or more but less than 20
if package_amount >= 10 and package_amount <= 19:
    print("You will get a 10% discount.")

#If the package amount is 20 or more but less than 50
elif package_amount >= 20 and package_amount <= 49:
    print("You will get a 20% discount.")

#If the package amount is 50 or more but less than 100
elif package_amount >= 50 and package_amount <= 99:
    print("You will get a 30% discount.")

#If the package amount is 100 or more
elif package_amount >= 100:
    print("You will get a 40% discount.")

#If the package amount is 10 or less
else:
    print("You will not get a discount.")
