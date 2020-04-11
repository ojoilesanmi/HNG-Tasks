#This will enable me to make use of the constant math.pi
import math 

print("Hi. This app calculates the area of a cirecle")

# The value the user enters is saved in the variable radius
radius = int(input("Enter the radius of the circle you want to calculate here: "))

#The formula for calculating the area of a circle
area = math.pi * (radius ** 2)

#To round up the answer to the nearest whole numnber to avoid unecessary decimal numbers
answer = math.ceil(area)

#Giving out the output- a formatted one
print("The Square of a circle with radius {0} is {1} ".format (radius, answer))