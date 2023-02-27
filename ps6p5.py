print("enter your last name")
lname = input()
print("enter your salary")
salary = float(input())
print("enter your job level")
jl = float(input())
if jl >= 10:
    brate = 0.25
else:
    if jl >= 5:
        brate = 0.2
    else:
        brate = 0.1
bonus = salary * brate
print("for" + lname + " the bonus is: $" + str(bonus))