# In a variable named number, take the input from the user and convert it to int.
# If this number is less than 10 then print "10 se chota hai". If it is greater than 10 and lesser than 20 then print "20 se chota hai".
#  Else if it is greater than 20 then print "20 se bada hai"
number=int(input("enter the numbe : r"))
if number>20:
    print("greater than 20")
elif number>10 and number<20 :
    print("less than 20")
else:
    print("less than 10")