#
# MIT OpenCourseWare 6.00C
# Problem Set 1
# Objective: Solve the same problem as for PS1b but using bisection search and calculating monthly payment to
#            the nearest cent: Write a program that calculates the minimum fixed monthly payment needed in order
#            to pay off a credit card balance within 12 months.
#
# Time: A lot...
#

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_payment_lower_bound = balance/12.0
monthly_payment_upper_bound = (balance*(1+(annual_interest_rate/12.0))**12.0)/12.0
monthly_payment = (monthly_payment_lower_bound+monthly_payment_upper_bound)/2.0
month = 1
numGuesses = 1
interest_paid = (annual_interest_rate/12)*balance
principal_paid = monthly_payment - interest_paid
remaining_balance = balance - principal_paid

while round(remaining_balance, 2) >= 0 and month < 12:
    month +=1
    interest_paid = (annual_interest_rate/12)*remaining_balance
    principal_paid = monthly_payment - interest_paid
    remaining_balance = remaining_balance - principal_paid

    if month == 12 and round(remaining_balance, 2) > 0.00:
        numGuesses += 1
        monthly_payment_lower_bound = round((monthly_payment+monthly_payment_lower_bound)/2.0, 3)
        monthly_payment = round((monthly_payment_lower_bound+monthly_payment_upper_bound)/2.0, 3)
        month = 0
        remaining_balance = balance

        
    elif month == 12 and round(remaining_balance, 2) < 0.00:
        numGuesses += 1
        monthly_payment_upper_bound = monthly_payment
        monthly_payment = round((monthly_payment_lower_bound+monthly_payment_upper_bound)/2.0, 3)
        month = 0
        remaining_balance = balance

       
print 'Monthly payment to pay off debt in 1 year: $',round(monthly_payment, 2)
print 'Number of months needed: ',month
print 'Balance: $',round(remaining_balance, 2)
print 'numGuesses: ',numGuesses
