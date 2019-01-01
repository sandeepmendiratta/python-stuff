#!/usr/bin/env python3

"""**Mortgage Calculator** -
Calculate the monthly payments of a fixed term mortgage
over given Nth terms at a given interest rate. Also figure
out how long it will take the user to pay back the loan."""

months = int(input("Enter mortgage term (in months): "))
rate = float(input("Enter interest rate: "))
loan = float(input("Enter loan value: "))

monthly_rate = rate / 100 / 12
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan


# print "Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f" % (loan, (months / 12), rate, payment)

print(f'Monthly payment for a ${loan} year mortgage at {monthly_rate}% interest rate is {rate} payment ${payment}')
print('Monthly payment for a ${} year mortgage at {}% interest rate is {} payment ${}'.format(loan, (months / 12), rate, payment))