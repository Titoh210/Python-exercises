# Exercise 01.2
# Calculate monthly mortgage interest

# Loan amount
principal = 172000

# Interest rates
boe_rate = 2.25
rate_over_boe = 1.49

# Total interest rate
total_rate = boe_rate + rate_over_boe

# Monthly interest calculation
interest = (principal * (total_rate / 100)) / 12

# Print result
print("Monthly interest payment:", interest)

#output
Monthly interest payment: 536.0666666666667