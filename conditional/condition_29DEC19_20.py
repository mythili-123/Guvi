# Write a program to input basic salary of an employee and calculate its Gross salary

bs=float(input("Enter your basic salary :\n"))
da=bs*0.6
hra=bs*0.15
gs=bs+da+hra
print("Your Gross Salary is: ",gs)