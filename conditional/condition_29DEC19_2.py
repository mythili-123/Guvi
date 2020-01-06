# Write a program to find maximum between three numbers.


a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

if(a>b) and (a>c):
 print(a)
elif(b>a) and (b>c):
 print(b)
else:
 print(c)
