# Declaring the recipe for 48 cookies to use in calculations
recipe_sugar = 1.5 #1.5 cups of sugar for 48 cookies
recipe_butter = 1 #1 cup of butter for 48 cookies
recipe_flour = 2.75 #2.75 cups of flour for 48 cookies
recipe_cookies = 48 #48 cookies with the above measurements

#Ask the user how many cookies they want to make
desired_cookies = int(input("How many cookies would you like to make?: "))

#Calculate the ratio of the amount of cookies the user wants compared to the starting amount
cookie_ratio = round(desired_cookies / recipe_cookies, 2)

#Calculate the amount of each ingredient needed for the desired amount of cookies, rounded to 2 decimal places
calculated_sugar = round(recipe_sugar * cookie_ratio, 2)
calculated_butter = round(recipe_butter * cookie_ratio, 2)
calculated_flour = round(recipe_flour * cookie_ratio, 2)

#Print the final amounts of each ingredient
print("You will need " + str(calculated_sugar) + " cups of sugar, \n" + str(calculated_butter) + " cups of butter, and \n" + str(calculated_flour) + " cups of flour.")
