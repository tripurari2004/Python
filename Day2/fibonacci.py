'''
Display Fibonacci series up to 10 terms.

*Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. 
The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34*
'''

num = int(input("Enter the number:- "))
num1,num2=0,1
for i in range(num):
    print(num1)
    
    next=num1+num2
    
    num1=num2
    num2=next