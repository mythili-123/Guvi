# Write a program to find sum of all odd numbers between 1 to n.

num=int(input("enter the number"))
i=1
sum=0
while i<=num:
 if i%2!=0:
  sum=sum+i
  print("the odd numbers are:")
 i=i+1
print("the sum of odd numbers are:",sum)