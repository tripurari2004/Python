'''Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.'''

x1=float(input("Enter the the value of x1:- "))
y1=float(input("Enter the the value of y1:- "))
x2=float(input("Enter the the value of x2:- "))
y2=float(input("Enter the the value of y2:- "))

distance = (((x2-x1)**2)+((y2-y1)**2))**0.5
print(f"The distance between two points {(x1,y1)} and {(x2,y2)} is {distance}")