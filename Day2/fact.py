'''
Write a program to use the loop to find the factorial of a given number.
'''

num = int(input("Enter the number:- "))
fact=1
for i in range(1,num+1):
    fact=fact*i

print(f"Factorial of {num} = {fact}")