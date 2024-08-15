'''
Write a program to print the following pattern

1

2 1

3 2 1

4 3 2 1

5 4 3 2 1

'''
num = int(input("Enter the number:- "))
for i in range(1,num+1):
    for k in range(i,0,-1):
        print(k,end=" ")
    print()