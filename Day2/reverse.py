'''
Reverse a given integer number.

Example:

Input: 76542
Output: 24567
'''

num = int(input("Enter the number:- "))
reverse=0
while(num>0):
    lastDigit=num%10
    reverse=reverse*10+lastDigit
    num=num//10

print(f"Reverse = {reverse}")