# create a simple console-based Python program
# that asks the user for the total bill, tip percentage, and the number of friends.
# It then calculates the tip and divides the remaining amount equally among all the friends.
print(f"Welcome to the tip calculator")
totalBill=float(input("What was the total bill? $"))
tipPercentage=int(input("What percentage tip would you like to give? "))
numberOfPeople=int(input("How many people to split the bill? "))
tip=(totalBill*(tipPercentage/100))
finalBill=totalBill+tip
billPerHead="{:.2f}".format(finalBill/numberOfPeople)
print(f"Each person should pay: ${billPerHead}")



