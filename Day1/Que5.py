'''Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
'''

principle = float(input("Enter the principle amount:- "))
rate = float(input("Enter the rate of Interest:- "))
timePeriod = float(input("Enter the time period in year:- "))

simpleInterest = (principle*rate*timePeriod)/100
totalAmount = principle+simpleInterest

print(f"Total interest = {simpleInterest}")
print(f"Total amount paid after {timePeriod} yrs = {totalAmount}")