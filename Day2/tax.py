'''
Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

Salary(Lakhs) : Tax(%)

*   Below 5 : 0%
*   5-10 : 10%
*   10-20 : 20%
*   aboove 20 : 30%
'''

salary = float(input("Enter the Yearly Salary in lakh:- "))
if salary<500000:
    salary=salary*0.82
elif salary<1000000:
    salary=salary*0.72
elif salary<2000000:
    salary=salary*0.62
else:
    salary=salary*0.52
    
print(f"Monthly hand salary = {round(salary/12,2)}")