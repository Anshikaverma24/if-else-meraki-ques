# If water in the filter is less than 1L then more water needs to be filled. 
# If the water quantity is between 1L and 10L then there is no need to fill water
# If water is more than 10L then the water will overflow. 
# For water level, take user input in a variable named water and convert it to an integer.

water=int(input("enter the water level : "))
if water>10:
    print("overflow")
elif water>1 and water<10:
    print("no need to fill the tank")
elif water<1:
    print("need to be filled more")

