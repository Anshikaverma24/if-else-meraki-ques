# Take two numbers as input from the user in variables varx and vary.
# Check whether varx is divisible by vary.
# If yes, print Divisible else print Not Divisible.

varx=int(input("enter first number : "))
vary=int(input("enter second number : "))
if varx%vary==0:
    print("divisible")
else:
    print("not divisible")