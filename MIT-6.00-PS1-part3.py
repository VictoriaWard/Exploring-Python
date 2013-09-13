# MIT Open Courseware - Introduction to Computer Science and Programming
# Problem Set 1 - Paying Off Credit Card Debt - Problem 3
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
Problem 3
Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance.

This is a version of problem 2, but here lower and upper bounds and a
bisection search are used to calculate the monthly payment to the
nearest penny.

lower bound is outstanding balance divided by 11 monthly payments
upper bound is outstanding balance plus compunded monthly interest for
12 months, divided by 11 monthly payments
"""


balance = float(input("Enter outstanding balance: "))
annual_interest = float(input("Enter annual interest rate as a percentage: "))/100
monthly_interest_rate = (annual_interest/12)

a = balance / 11    #lower bound
b = (balance * (1 + (annual_interest/12)) ** 12) / 11    #upper bound

updated_balance = balance
monthly_payment = (a + b) / 2
for m in range(11):
        updated_balance = updated_balance * (1 + monthly_interest_rate) - monthly_payment
while not 0 >= updated_balance >= -1 :
    if updated_balance > 0:
        a += .01
    elif updated_balance < 1:
        b -= .01
    updated_balance = balance
    monthly_payment = (a + b) / 2         
    for m in range(11):
        updated_balance = updated_balance * (1 + monthly_interest_rate) - monthly_payment

print("\nMonthy payment to pay off debt in 1 year: £" + str(round(monthly_payment, 2)) + "\nMonths needed: 11" + "\nBalance: £" + str(round(updated_balance, 2)))








