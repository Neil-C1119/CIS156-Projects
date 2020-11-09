#This program asks the user for one or several names and will tell the user whether
#the name(s) they typed are in the top 200 boy or girl names

try:
    boy_list = [] #List for the boy names
    girl_list = [] #List for the girl names

    with open("GirlNames.txt", "r") as GirlNames: #Open the girl names document and push each of the names into the list for girl names
        lines = GirlNames.readlines()
        for name in lines:
            girl_list.append(name.strip("\n"))

    with open("BoyNames.txt", "r") as BoyNames: #Open the girl names document and push each of the names into the list for boy names
        lines = BoyNames.readlines()
        for name in lines:
            boy_list.append(name.strip("\n"))

    user_name = input("Enter a boy or girl's name or both: ") #Ask the user for the names

    if len(user_name.split()) > 1: #If there is more than one name the user typed
        for input in user_name.split(): #For each name the user typed
            no_name = "T" #Variable to track whether the name is in one of the lists or not
            for name in boy_list: #For each name in the boy name list check if the name equals the user's name
                if input == name.lower(): #If the name is in there tell the user it's in the top 200 names and change the no_name variable
                    print(name.upper(), "is in the top 200 names for boys.")
                    no_name = "F"
            for name in girl_list: #For each name in the girl name list check if the name equals the user's name
                if input == name.lower(): #If the name is in there tell the user it's in the top 200 names and change the no_name variable
                    print(name.upper(), "is in the top 200 names for girls.")
                    no_name = "F"
            if no_name == "T": #If the name is not in either of the lists tell the user
                print(input.upper(), "is not in the top 200 names for boys or girls.")

    elif len(user_name.split()) == 1: #If there is only one name that the user typed
        no_name = "T" #Variable to track whether the name is in one of the lists or not
        for name in boy_list: #For each name in the boy list check if the name equals the user's name
            if user_name == name.lower(): #If the name is in there tell the user it's in the top 200 names and change the no_name variable
                print(name.upper(), "is in the top 200 names for boys.")
                no_name = "F"

        for name in girl_list: #For each name in the girl list check if the name equals the user's name
            if user_name == name.lower(): #If the name is in there tell the user it's in the top 200 names and change the no_name variable
                print(name.upper(), "is in the top 200 names for girls.")
                no_name = "F"
        if no_name == "T": #If the name is not in either of the lists tell the user
            print(name.upper(), "is not in the top 200 names for boys or girls.")

except IOError: #If there is an error finding the file tell the user
    print("Could not find one or more of the name files. . .")
