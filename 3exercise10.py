penny = .01
nickel = .05
dime = .1
quarter = .25

print("Make a dollar to win!")

pennyAmt = int(input("\nHow many pennies?: ")) * penny
nickelAmt = int(input("\nHow many nickels?: ")) * nickel
dimeAmt = int(input("\nHow many dimes?: ")) * dime
quarterAmt = int(input("\nHow many quarters?: ")) * quarter

total = pennyAmt + nickelAmt + dimeAmt + quarterAmt

if total == 1:
    print("\nPerfect! You made a dollar.")
elif total > 1:
    print("\nToo bad. You went over a dollar.")
elif total < 1:
    print("\nToo bad. You were under a dollar.")

input("Press enter to end the script. . .")
