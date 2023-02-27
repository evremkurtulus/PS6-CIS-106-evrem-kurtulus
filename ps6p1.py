print("enter quantity of widgets.")
qty = float(input())
if qty > 10000:
    price = 10
else:
    if qty > 5000:
        price = 20
    else:
        price = 30
extprice = price * qty
tax = extprice * 0.07
total = extprice + tax
print("for" + str(qty) + " widget/s, the price is: $" + str(price) + ", so, the extended price is: $" + str(extprice))
print("plus tax (7%): $" + str(tax))
print("the total for the order will be: $" + str(total))
