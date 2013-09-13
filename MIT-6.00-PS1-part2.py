# MIT Open Courseware - Introduction to Computer Science and Programming
# Problem Set 1 - Paying Off Credit Card Debt - Problem 2
# by Victoria Ward

"""
Paying Off Credit Card Debt

Each month, a credit card statement will come with the option for you
to pay a minimum amount of your charge, usually 2% of the balance due.
However, the credit card company earns money by charging interest on
the balance that you don’t pay. So even if you pay credit card
payments on time, interest is still accruing on the outstanding
balance.

Paying Debt Off In a Year
Problem 2
Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance.

Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less than 12) it takes to pay off the debt,
and the balance (likely to be a negative number).
Assume that the interest is compounded monthly according to the balance at the start of the month (before the payment for that month is made).
The monthly payment must be a multiple of 10 and is the same for all months.
Notice that it is possible for the balance to become negative using this payment scheme. 
"""


balance = float(input("Enter outstanding balance: "))
annual_interest = float(input("Enter annual interest rate as a percentage: "))/100
monthly_interest_rate = (annual_interest/12)

updated_balance = balance
monthly_payment = 0
while updated_balance > 0:
    updated_balance = balance
    monthly_payment += 10
    for m in range(11):
        updated_balance = updated_balance * (1 + monthly_interest_rate) - monthly_payment

print("\nMonthy payment to pay off debt in 1 year: £" + str(monthly_payment) + "\nMonths needed: 11" + "\nBalance: £" + str(round(updated_balance, 2)))








