#Test average and letter grade

#Start an empty array to add scores to
score_array = []

#The function that adds the user's scores to the array
def array_population():
    #Ask the user for the test score and add to the end of the array
    score1 = float(input("Type in the first score: "))
    score_array.append(score1)
    #etc.
    score2 = float(input("\nType in the second score: "))
    score_array.append(score2)
    #etc.
    score3 = float(input("\nType in the third score: "))
    score_array.append(score3)
    #etc.
    score4 = float(input("\nType in the fourth score: "))
    score_array.append(score4)
    #etc.
    score5 = float(input("\nType in the fifth score: "))
    score_array.append(score5)

#The function that calculates the average of all the scores
def calc_average(score1st, score2nd, score3rd, score4th, score5th):
    #Add each score and divide the total by 5
    average = (score1st + score2nd + score3rd + score4th + score5th) / 5
    #Return the average score
    return average

#The function that determines a score's letter grade
def determine_grade(test_score):
    #If the score is above 90
    if test_score >= 90:
        #Return the letter A
        return "A"
    #If the score is above 80
    elif test_score >= 80:
        #Return the letter B
        return "B"
    #If the score is above 70
    elif test_score >= 70:
        #Return the letter C
        return "C"
    #If the score is above 60
    elif test_score >= 60:
        #Return the letter D
        return "D"
    #If the score is anything else
    else:
        #Return the letter F
        return "F"

#Call the array_population function
array_population()

#Print the average score by calling the calc_average function with each of the test scores as arguments
print("\nYour average score between all 5 tests was ---> " + str(calc_average(score_array[0], score_array[1], score_array[2], score_array[3], score_array[4])))

#For loop that goes through each score in the array and...
for score in score_array:
    #Creates a variable that calls the determine_grade function with that score as the argument
    letter_grade = determine_grade(score)
    #Print the score and letter grade
    print("\nThe letter grade for", score, "is a(n) --->", letter_grade)

input("\nPress enter to exit. . .")
