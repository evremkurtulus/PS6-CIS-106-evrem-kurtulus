print("enter the principle amount of the CD")
prin = float(input())
print("enter the year to maturity")
year = float(input())
if prin > 100000 and year == 5:
    rate = 0.06
else:
    if prin > 50000 and year == 10:
        rate = 0.05
    else:
        if prin > 50000 and year == 5:
            rate = 0.04
        else:
            rate = 0.02
interest = prin * rate
print("for the principle of $" + str(prin) + ", for the first year the interest rate is: " + str(rate) + ". And the interest amount for the first year is: $" + str(interest))
