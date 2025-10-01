import math
#Enter radius and define pi
r_circle=int(input("Enter radius of a circle:"))
pi= 3.14159

#Compute the area of a circle
area_circle= pi* pow(r_circle,2)
finalarea= round(area_circle,2)
#Display the result
print("The area of a circle is:", finalarea, "square units")