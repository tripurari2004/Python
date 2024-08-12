'''
Write a menu-driven program -
1. cm to ft
2. km to miles
3. USD to INR
4. exit
'''

menu = int(input('''
Write a menu-driven program -
1. cm to ft
2. km to miles
3. USD to INR
4. exit
'''))

if(menu==1):
    cm=float(input("Enter the value:- "))
    print(f"{cm} cm = {0.032*cm} ft")
elif(menu==2):
    km=float(input("Enter the value:- "))
    print(f"{km} km = {0.62*km} miles")
elif(menu==3):
    usd=float(input("Enter the value:- "))
    print(f"{usd} USD = {80*usd} INR")
else:
    exit()