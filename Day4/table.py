'''
Write a program to print multiplication table of a given number
'''

num = int(input("Enter the number:- "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")