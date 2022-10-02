
# Program to calculate the mortgage

#create a variable "principal" to take input from the user 
# Use the input method to ask the user for input on the command line
#Because the the input is most likely has decimals we pass the "input method" into the float method
# to convert the user input into a float in order to handle computation involving decimals.



principal = float(input("Mortgage loan Principal:  "))


# The rate of interest divided by 12 months
annual_rate_of_interest = float(input("Percent Annual Interest: "))
monthly_interest = annual_rate_of_interest/(100*12)

#Years to pay back Loan
years= float(input("Years to Pay off Mortgage: "))


# Number of months to make repayment 
numberOfPayments = years * 12


# from the formular given

monthlyRepaymentCost = (principal * (monthly_interest * ( 1 + monthly_interest)** numberOfPayments)) / ((1+monthly_interest) ** numberOfPayments - 1)
total_charge = (monthlyRepaymentCost * numberOfPayments) 


print('For a {0}-year mortgage loan of ${1:,} \nat an annual interest rate of {2}% \nYou pay \n  ${3} monthly \nTotal amount paid will be ${4:,}'.format(int(years), round(principal, 2), annual_rate_of_interest, round(monthlyRepaymentCost, 2), round(total_charge, 2)))

# to run the file in the vs code terminal 
# py -3 mortgagecalculator.py
# The test example was passed







