red = "red"
yellow = "yellow"
blue = "blue"
firstColor = input("Choose a primary color to mix, then hit enter. : ")

if firstColor == (red or yellow or blue):
    secondColor = input("Choose another primary color to mix, then hit enter. : ")

    if (secondColor != firstColor) and secondColor == red or secondColor == yellow or secondColor == blue:

        if (firstColor == red and secondColor == blue) or (firstColor == blue and secondColor == red):
            print("You mixed " + firstColor + " and " + secondColor + " and got purple!")

        if (firstColor == red and secondColor == yellow) or (firstColor == yellow and secondColor == red):
            print("You mixed " + firstColor + " and " + secondColor + " and got orange!")

        if (firstColor == blue and secondColor == yellow) or (firstColor == yellow and secondColor == blue):
            print("You mixed " + firstColor + " and " + secondColor + " and got green!")

    elif secondColor == firstColor:
        print("You picked the same color for both, try again.")
    else:
        print("That isn't a primary color, try again.")

else:
    print("That isn't a primary color, try again.")

input("Press enter to end the script. . .")
