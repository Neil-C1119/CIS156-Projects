#This program asks the user for a baseball team and will tell them whether or not
#the team has won a World Series, and if they have how many times

#This program works if you only type one part of a team's name as well, like the
#mascot or city/state it's from

try:
    wins = 0 #Variable to keep track of how many wins the team has
    user_input = input("Type the name of a baseball team: ") #Variable to hold what the user types
    user_team = "" #Variable to hold the full name of the team

    with open("WorldSeriesWinners.txt", "r") as WS_winners: #Open the World Series Winners text file as a variable
        lines = WS_winners.readlines() #Variable that makes a list of each line of the World Series winners
        for team in lines: #For each team in the file
            team_str = team.strip("\n") #Variable that holds the team's name without the newline character
            if user_input.upper() in team_str.upper(): #If what the user typed is somewhere in one of the team's names
                wins += 1 #Add a win
                user_team = team_str.upper() #Set the user's team to equal that team's full name in the list

    if wins > 0: #If the team has more than one win tell the user how many wins they have
        print("The", user_team, "have won the World Series", wins, "time(s).")

    else: #If the team doesn't have any wins tell the user
        print("The team you chose has not won the World Series yet.")

except IOError: #If there is an error finding the file tell the user
    print("Could not find the WorldSeriesWinners.txt file. . .")
