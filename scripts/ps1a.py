#
# MIT OpenCourseWare 6.00
# Problem Set 1
# Problem 1
# Author: Niculin
# Objective: Write a program to calculate the credit card balance after one year if a person only pays the 
#            minimum monthly payment required by the credit card company each month. 
#            Use raw_input() to ask for the following three floating point numbers: 
#               1. the outstanding balance on the credit card 
#               2. annual interest rate 
#               3. minimum monthly payment rate 
#            For each month, print the minimum monthly payment, remaining balance, principle paid in the 
#            format shown in the test cases below. All numbers should be rounded to the nearest penny. 
#            Finally, print the result, which should include the total amount paid that year and the remaining 
#            balance. 
# Time: 2:00
#

balance = float(raw_input('Enter the outstanding balance: '))
annual_interest_rate = float(raw_input('Enter the annual interest rate as a decimal: '))
minimum_monthly_payment_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
month = 1
minimum_monthly_payment = minimum_monthly_payment_rate*balance
interest_paid = (annual_interest_rate/12)*balance
principal_paid = minimum_monthly_payment - interest_paid
remaining_balance = balance - principal_paid
amount_paid = minimum_monthly_payment

while month <= 12:
    print 'Minimum monthly payment for month ',month,'is: $',round(minimum_monthly_payment, 2)
    print 'Principal paid for month ',month,'is: $',round(principal_paid, 2)
    print 'Remaining balance for month ',month,'is: $',round(remaining_balance, 2)
    if month < 12:
        month += 1
        minimum_monthly_payment = minimum_monthly_payment_rate*remaining_balance
        interest_paid = (annual_interest_rate/12)*remaining_balance
        principal_paid = minimum_monthly_payment - interest_paid
        remaining_balance = remaining_balance - principal_paid
        amount_paid += minimum_monthly_payment
    else:
        break
print 'Total amount paid for the year is: $',round(amount_paid, 2)
print 'Remaining balance is: $',round(remaining_balance, 2)
