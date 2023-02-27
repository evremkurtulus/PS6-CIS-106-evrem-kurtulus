print("enter number of tickets")
qty = float(input())
if qty >= 25:
    ppt = 50
else:
    if qty >= 10:
        ppt = 60
    else:
        if qty >= 5:
            ppt = 70
        else:
            ppt = 75
total = qty * ppt
print("for " + str(qty) + " tickets, the price per ticket is: $" + str(ppt) + ". The total comes up to: $" + str(total))
