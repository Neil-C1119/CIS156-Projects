#Popultation

#Define the population function
def popFunc():

    #Getting starting values from the user
    starting_amount = int(input("How many organisms to start with? "))
    daily_increase = int(input("What percent of daily increase? ")) / 100
    days = int(input("How many days will this last? "))

    #Set the running amount to begin at the starting amount
    running_amount = starting_amount

    #Print the first day's amount
    print("\nDay 1 starts with", starting_amount, "organisms")

    #For each day starting at 2 until the day the user sets, including that day
    for day in range(2,days + 1):

        #Add a calculated amount to the current running amount
        running_amount = running_amount + (running_amount * daily_increase)

        #Show the user that day's results
        print("\nDay", day, "had", "{:.2f}".format(running_amount), "organisms.")

popFunc()
