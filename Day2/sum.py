'''
Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number.  Print the final result. And don't use for loop to solve this problem.

'''

num = int(input("Enter the number:- "))
sum=0
for i in range(1,num+1):
    if i%5==0:
        continue
    sum+=i
    
print(f"Sum of number = {sum}")