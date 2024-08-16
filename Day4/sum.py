'''
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
'''

num = int(input("Enter the number:- "))
sum=0
for i in range(1,num+1):
    sum += i
print("Sum is: ",sum)