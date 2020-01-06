# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle 

x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value of z:"))
if(x==y==z):
 print("triangle is equilateral")
elif(x==y) or (y==z) or (x==z):
 print("triangle is isosceles")
else:
 print("triangle is scalene")