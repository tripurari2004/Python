'''
Print the following pattern.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

num = int(input("Enter the number:- "))
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
   
for k in range(num-1,0,-1):
    for l in range(k,0,-1):
        print("*",end=" ")
    print()