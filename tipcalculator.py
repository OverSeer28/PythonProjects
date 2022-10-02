


#Program to calculate Tip and Sales Tax in a Resturant



#create a file called tipcalculator.py
# Create a variable called 'charge_for_food' to receive the input
# Use the input method to ask the user for input on the command line
#Because the the input is most likely has decimals we pass the "input method" into the float method
# to convert the user input into a float in order to handle computation involving decimals.

charge_for_food = float(input("Charge For Food in GH₵: "))

# we the multply 0.18 by the charge_for_food to obtain the tip and assign it to the Tip variable
Tip = 0.18 * charge_for_food 

# we the multply 0.07 by the charge_for_food to obtain the tip and assign it to the Sales_Tax variable
Sales_Tax = 0.07 * charge_for_food 

# calculate the total amount and assign it to the Total_Amount 
Total_Amount = charge_for_food + Tip + Sales_Tax

# Display the results to the terminal with the print function
# the round method is used to round to 2 decimal places
print("Tip = GH₵", round(Tip, 3) )
print("Sales Tax = GH₵", round(Sales_Tax, 3) )
print("Grand Total = GH₵", round(Total_Amount, 3))


# to run the file in the vs code terminal 
# py -3 tipcalculator.py


# The test example was passed
