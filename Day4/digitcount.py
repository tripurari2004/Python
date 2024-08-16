'''
Write a program to count the total number of digits in a number using a while loop.
'''

num= int(input("Enter the number:- "))
digit=0
while(num>0):
    lastdigit = num%10
    digit +=1
    num //=10
    
print(digit)