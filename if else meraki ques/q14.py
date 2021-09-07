# People 5 years and above in age can go to school.
# People 18 years and above in age can vote in elections.
# People 21 years and above in age can drive a car.
# People 24 years and above in age can marry.
# People 25 years and above in age can legally drink.
# takes the age of the user as input. Print what all activities the user can do from the list above. 

age=int(input("enter the age : "))
a="can legally drink"
b="can marry"
c="can drive"
d="can vote"
e="can go to school"
if age>=25:
    print(a,b,c,d,e)
elif age>=24:
    print(b,c,d,e)
elif age>=21:
    print(c,d,e)
elif age>=18:
    print(d,e)
elif age>=5:
    print(e)
