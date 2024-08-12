'''
Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
'''

costPrice = float(input("Enter the Cost Price:- "))
selligPrice = float(input("Enter the Selling Price:- "))

if(selligPrice>costPrice):
    print(f"Profit is equal to {selligPrice-costPrice}")
elif(costPrice>selligPrice):
    print(f"Loss is equal to {costPrice-selligPrice}")
else:
    print("No Profit No loss")