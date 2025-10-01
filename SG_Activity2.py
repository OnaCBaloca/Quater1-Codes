import math
#Ask for all the variables from user
x_1= int(input("Enter x1:"))
x_2= int(input("Enter x2:"))
y_1= int(input("Enter y1:"))
y_2= int(input("Enter y2:"))

#Start computation
d= math.sqrt(pow(x_2 - x_1,2) + pow(y_2 - y_1,2))

finald= round(d,2)

#Display the result
print("The distance between two points are:", finald)