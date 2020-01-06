# Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input("Enter the First Angle of a Triangle:"))
b = int(input("Enter the Second Angle of a Triangle:"))
c = int(input("Enter the Third Angle of a Triangle:"))

total = a + b + c

if total == 180:
    print("\nThis is a Valid Triangle")
else:
    print("\nThis is an Invalid Triangle")
