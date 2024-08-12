'''
Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
'''

angle1 = int(input("Enter the first angle:- "))
angle2 = int(input("Enter the second angle:- "))
angle3 = int(input("Enter the third angle:- "))

if(angle1+angle2+angle3==180 and angle1>0 and angle2>0 and angle3>0):
    print(f"{angle1},{angle2},{angle3} form a triangle")
else:
    print(f"{angle1},{angle2},{angle3} not form a triangle")