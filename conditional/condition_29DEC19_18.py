# Write a program to calculate profit or loss.


ac=float(input("enter the actual cost:"))
sa=float(input("enter the sale amount:"))
if(ac>sa):
 amount=ac-sa
 print("total loss amount")
elif(sa>ac):
 amount=sa--ac
 print("total profit amount")
else:
 print("no profit")