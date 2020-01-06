# Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1=int(input("enter a side1:"))
side2=int(input("enter a side2:"))
side3=int(input("enter a side3:"))


if((side1+side2)>side3)or((side1+side3)>side2)or((side2+side3)>side1):
 print("triangle is valid")
else:
 print("invalid triangle")