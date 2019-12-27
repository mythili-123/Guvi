# Write a program to find sum of all natural numbers between 1 to n.

num=5
if num<0:
 print("enter the number")
else:
 sum=0
 while(num>0):
   sum+=num
   num-=1
   print("sum is:",sum)