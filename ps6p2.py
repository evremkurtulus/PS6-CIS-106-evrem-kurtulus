print("enter part number")
pn = input()
print("enter quantity")
qty = float(input())
if pn == "10" or pn == "55":
    costpu = 1
else:
    if pn == "99":
        costpu = 2
    else:
        if pn == "80" or pn == "70":
            costpu = 3
        else:
            costpu = 5
total = qty * costpu
print("for part number #" + pn + " the cost per unit will be: $" + str(costpu) + ", and the total cost is: $" + str(total))
