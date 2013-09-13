# MIT Open Courseware - Introduction to Computer Science and Programming
# Problem Set 1 - Paying Off Credit Card Debt
# by Victoria Ward

"""
Paying Off Credit Card Debt

Each month, a credit card statement will come with the option for you
to pay a minimum amount of your charge, usually 2% of the balance due.
However, the credit card company earns money by charging interest on
the balance that you don’t pay. So even if you pay credit card
payments on time, interest is still accruing on the outstanding
balance.

Paying the Minimum
Problem 1
Write a program to calculate the credit card balance after one year if
a person only pays the minimum monthly payment required by the credit
card company each month.

For each month, print the minimum monthly payment, remaining balance, principle paid.
All numbers should be rounded to the nearest penny.
Finally, print the result, which should include the total amount paid that year and the remaining balance.
"""


month = 1
balance = float(input("Enter outstanding balance: "))
annual_interest = float(input("Enter annual interest rate as a percentage: "))/100
minimum_monthly_rate = float(input("Enter minimum monthly payment rate as a percentage: "))/100
for m in range(12):
    minimum_monthly_payment = minimum_monthly_rate * balance
    monthly_interest = (annual_interest/12) * balance
    principal_paid = minimum_monthly_payment - monthly_interest
    balance = balance - principal_paid
    print ("\nMonth", month, "\nMinimum monthly payment: £", (round(minimum_monthly_payment, 2)), "\nPrincipal paid: £",round(principal_paid, 2),
           "\nRemaining balance: £",round(balance,2))
    month += 1





