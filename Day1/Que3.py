'''Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.'''

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))

temp = num2
num2 = num1
num1 = temp

print(num1,num2)