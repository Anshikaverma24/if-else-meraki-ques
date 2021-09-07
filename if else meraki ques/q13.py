#  take a number as user input. Check if this number is divisible by 5 and 15 both.
num=int(input("enter the number : "))
if num%5==0 and num%15==0:
    print("divisible by 5 and 15")
else:
    print("not divisible")