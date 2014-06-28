#
# MIT OpenCourseWare 6.00C
# Problem Set 1
# Objective: Now write a program that calculates the minimum fixed monthly payment needed in order pay 
#           off a credit card balance within 12 months.
# Time:
#

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_payment = 10
month = 1
interest_paid = (annual_interest_rate/12)*balance
principal_paid = monthly_payment - interest_paid
remaining_balance = balance - principal_paid

while remaining_balance >= 0 and month < 12:
    month +=1
    interest_paid = (annual_interest_rate/12)*remaining_balance
    principal_paid = monthly_payment - interest_paid
    remaining_balance = remaining_balance - principal_paid

    if month == 12 and remaining_balance > 0:
        monthly_payment += 10
        month = 0
        remaining_balance = balance
        
print 'Monthly payment to pay off debt in 1 year: $',monthly_payment
print 'Number of months needed: ',month
print 'Balance: $',round(remaining_balance, 2)
